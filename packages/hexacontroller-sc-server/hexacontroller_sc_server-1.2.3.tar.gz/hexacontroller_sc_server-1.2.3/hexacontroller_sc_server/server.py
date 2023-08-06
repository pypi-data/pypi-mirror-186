from schema import Schema, Or, Optional, SchemaError
import zmq
import yaml
import logging

from . import i2c_utilities
from .Hexaboard import Hexaboard


cmd_schema_recv = Schema({'type':
                          Or('set', 'get', 'describe', 'reset', 'stop'),
                          Optional('read_back', default=False): bool,
                          Optional('from_hardware', default=False): bool,
                          'status': 'send',
                          'args': dict})


class Server():
    """
    Server to unpack requests from a client, interface with the Hexaboard,
    and pack and send resulting messages to the client
    """

    def __init__(self, port, regmap_table):
        """
        Creates hexaboard and opens socket for receiving requests

        :param port: Port to open a socket on
        :type port: int
        :param regmap_table: Table containing configuration parameter
            definitions for the ROCs on the hexaboard
        :type regmap_table: str
        """
        self.logger = logging.getLogger()
        context = zmq.Context()
        self.socket = context.socket(zmq.REP)
        self.socket.bind(f'tcp://0.0.0.0:{port}')
        try:
            board_type, description = i2c_utilities.find_links()
            self.hexaboard = Hexaboard(board_type, description, regmap_table)
        except IndexError as e:
            self.logger.critical(f'{e.args[0]}', exc_info=True)
            print("Unable to initialize the hardware")
            exit(1)

    def run(self):
        """
        Starts and runs the server which listens on the port used to
        instantiate the Server object
        """
        while True:
            try:
                client_request = yaml.safe_load(self.socket.recv())
                client_request, errors = self._validate_request(client_request)
                if errors is not None:
                    self._respond(client_request['type'], error=errors)
                else:
                    match client_request['type']:
                        case 'get':
                            try:
                                response_args = self.hexaboard.read(
                                        client_request['args'],
                                        client_request['from_hardware'])
                                self._respond('get', response_args)
                            except (KeyError, ValueError, IOError) as error:
                                self._respond('get', error=error.args[0])
                        case 'set':
                            try:
                                self.hexaboard.configure(
                                        client_request['args'],
                                        client_request['read_back'])
                                self._respond('set')
                            except (KeyError, ValueError, IOError) as error:
                                self._respond('set', error=error.args[0])
                        case 'describe':
                            response_args = self.hexaboard.describe()
                            self._respond('describe', response_args)
                        case 'reset':
                            self.hexaboard.reset()
                            self._respond('reset')
                        case 'stop':
                            self._respond('stop')
                            break
            except KeyboardInterrupt:
                break
        return

    def _validate_request(self, client_request):
        """
        Checks that the request from the client has the expected structure.

        :param client_request: Request message received from the client
        :type client_request: dict
        :return: Errors in client_request structure or None if request is valid
        :rtype: str
        """
        try:
            client_request = cmd_schema_recv.validate(client_request)
        except SchemaError as error:
            self.logger.error(f'Message is invalid: "{error}"')
            return (client_request, error.args[0])
        else:
            self.logger.info("Received request of type "
                             f"{client_request['type']}")
            self.logger.debug("Recieved request contains args "
                              f"{client_request['args']}")
            return (client_request, None)

    def _respond(self, type, response_args={}, error=None):
        """
        Sends a response message to the client.

        :param type: Type of request server is responding to
        :type type: str
        :param response_args: Arguments to pass back to client. Typically
            configurations from the hexaboard
        :type response_args: dict, optional
        :param error: Error message to send if an error occured
        :type error: str, optional
        """
        server_response = {'type': type,
                           'status': 'success',
                           'args': response_args}
        if error is not None:
            server_response['status'] = 'error'
            server_response['errmsg'] = error
        self.socket.send_string(yaml.dump(server_response, sort_keys=False))

    def __del__(self):
        self.socket.close()
        self.logger.info("Closing i2c server...")
        print("Closing server...")
