'''Socket Server SSL Module'''
import sys
import time
import traceback
import socket
from socketserver import TCPServer, BaseRequestHandler
import ssl
from pyZynoUnifiedDrivers.miva.module_utils import download_mfg_32_bit, download_miva_8_bit, download_miva_32_bit
PRIVATE_KEY_PATH = './miva/server_key_store/private_key.pem'
SERVER_CERTIFICATE_PATH = './miva/server_key_store/certificate.crt'

_TIMEOUT = 0.025

SOCKET_BUFFER_SIZE = 4096


class SocketRequestHandlerSSL(BaseRequestHandler):
    """
    The request handler class for our server.
 
    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """
 
    def handle(self):
        try:
            if (self.server.is_on()):
                # self.request is the TCP socket connected to the client
                self.data = self.request.recv(SOCKET_BUFFER_SIZE)
                # print('self.data = {}'.format(self.data))
                if self.data == b'':
                    # break if client closes the socket
                    pass
                    # break            
                elif self.data == b'\r\n':
                    # ignore [\r\n]
                    pass
                    # continue
                else:
                    #
                    print('{}'.format(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())))
                    # print(self.data)
                    # just send back the same data, but upper-cased
                    # self.request.sendall(self.data + b'\r\n')
                    # self.request.sendall(b'server status: ' + str(self.server.is_on()).encode() + b'\r\n')
                    message = self.data.decode(errors='ignore').strip(' \t\r\n\0')
                    print('get: \'{0}\' from {1}'.format(message, self.client_address[0]))
                    # print('length = {}'.format(len(message)))
                    # print()
                    if self.server.miva != None:
                        if message.lower() in [':download:mfg32', ':flash:mfg32', ':install:mfg32']:
                            return_message = download_mfg_32_bit()
                            if return_message:
                                return_message = 'Success: Download [mfg 32-bit firmware] with [pyProgrammerCLI.exe]'
                            else:
                                return_message = 'Fail: Download [mfg 32-bit firmware] with [pyProgrammerCLI.exe]'
                        elif message.lower() in [':download:miva8', ':flash:miva8', ':install:miva8']:
                            return_message = download_miva_8_bit()
                            if return_message:
                                return_message = 'Success: Download [miva 8-bit firmware] with [FlashUtilCL.exe]'
                            else:
                                return_message = 'Fail: Download [miva 8-bit firmware] with [FlashUtilCL.exe]'
                        elif message.lower() in [':download:miva32', ':flash:miva32', ':install:miva32']: 
                            return_message = download_miva_32_bit()
                            if return_message:
                                return_message = 'Success: Download [miva 32-bit firmware] with [pyProgrammerCLI.exe]'
                            else:
                                return_message = 'Fail: Download [miva 32-bit firmware] with [pyProgrammerCLI.exe]'
                        else:
                            return_message = self.server.miva.query(message)
                        # print('return_message = {}'.format('\'\'' if return_message == '' else return_message))
                    else:
                        return_message = self.server.process_incomming_message(message)                        
                    if return_message != '':
                        #
                        data = return_message.strip(' \t\r\n\0').encode()
                        self.request.sendall(data)
                        print('sent: \'{0}\''.format(return_message))
                        print()
        except socket.timeout:
            traceback.print_exc()
        except UnicodeDecodeError:
            print()
            # print("{0}: {1}\n".format(sys.exc_info()[0], sys.exc_info()[1]))
            traceback.print_exc()
        except (ConnectionResetError, OSError):
            print()
            print('{0}: {1}\n'.format(sys.exc_info()[0], sys.exc_info()[1]))
        except:
            traceback.print_exc()
        finally: 
            self.request.close()
            return ''


class SocketServerSSL(TCPServer): 

    def __init__(self,
                 server_address,
                 RequestHandlerClass,
                 certfile,
                 keyfile,
                 ssl_version=ssl.PROTOCOL_TLSv1,
                 bind_and_activate=True,
                 miva=None):
        '''__init__'''
        TCPServer.__init__(self, server_address, RequestHandlerClass, bind_and_activate)
        self.certfile = certfile
        self.keyfile = keyfile
        self.ssl_version = ssl_version
        
        self.HOST, self.PORT = server_address
        self._is_on = False
        self.miva = miva     

    def get_request(self):
        newsocket, fromaddr = self.socket.accept()
        connstream = ssl.wrap_socket(newsocket,
                                 server_side=True,
                                 certfile=self.certfile,
                                 keyfile=self.keyfile,
                                 ssl_version=self.ssl_version)
        return connstream, fromaddr

    def start(self):
        '''start ssl server'''
        try:
            # print("Socket server started at [{}]"\
            # .format(time.strftime('%H:%M:%S', time.localtime())))
            self.set_on()
            self.serve_forever()
            print("Socket server stopped at [{}]"\
                    .format(time.strftime('%H:%M:%S', time.localtime())))
        except KeyboardInterrupt:
            print('Exiting: [Ctrl + C] is pressed')
            pass        
        except OSError:
            print('Exiting: [OSError] is captured')
            pass
        except:
            traceback.print_exc()
            pass
        finally:
            self.stop()
        
    def stop(self):
        '''stop'''
        self.shutdown()
        self._is_on = False
        # print("Socket server stopped at [{}]"\
        # .format(time.strftime('%H:%M:%S', time.localtime())))
    
    def set_on(self):
        '''stop'''
        self._is_on = True
        print('Socket server [{}] is listening on port [{}]'.format(self.HOST, self.PORT))    
        print()
        
    def is_on(self):
        '''is on'''
        return self._is_on
    
    def status(self):
        if self._is_on:
            print("Gateway Server: [On]")
            print("\t{0:5}: {1}".format('IP', self.HOST))
            print("\t{0:5}: {1}".format('Port', str(self.PORT)))
        else:
            print("Gateway Server: [Off]")

    def process_incomming_message(self, cmd):
        if cmd.lower().strip(' \t\r\n\0') == '*idn?':
            return_msg = 'Socket Server SSL ({})'.format(self.HOST)        
        else:
            return_msg = ''
        return return_msg

        
def main():
    '''main function'''
    try:
        hostname = socket.gethostname()
        local_ip = socket.gethostbyname(hostname)
        # local_ip = '192.168.0.19'
        # print("IP Address: {0}".format(local_ip))
    
        # HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
        HOST = local_ip
        PORT = 443  # Port to listen on (non-privileged ports are > 1023)
        # Create the server, binding to localhost on port 65432
        with SocketServerSSL((HOST, PORT),
                             SocketRequestHandlerSSL,
                             certfile=SERVER_CERTIFICATE_PATH,
                             keyfile=PRIVATE_KEY_PATH,) as socket_server_ssl:
            socket_server_ssl.start()
    except KeyboardInterrupt:
        print('Exiting: [Ctrl + C] is pressed')
        pass


if __name__ == "__main__":
    main()
