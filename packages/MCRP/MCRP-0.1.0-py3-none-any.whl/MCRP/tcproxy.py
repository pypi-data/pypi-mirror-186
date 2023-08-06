import socket
import threading
import traceback
import typing
import time

class tcproxy:

    Client: socket.socket
    Server: socket.socket

    ClientFactory: socket.socket
    UpstreamAddr: tuple

    def _waiting_for_client(self):
        pass

    def _new_client(self):
        pass
    
    def _new_server(self):
        pass
    
    def _client_lost(self):
        pass
    
    def _server_lost(self):
        pass
    
    def _from_client(self, data):
        pass
    
    def _from_server(self, data):
        pass
    
    def _server_error(self, error):
        pass

    def __init__(self, listen_addr: tuple, upstream_addr: tuple):

        self.ClientFactory = socket.socket(2, 1)
        self.ClientFactory.bind(listen_addr)
        self.ClientFactory.listen(1)
        
        self.UpstreamAddr = upstream_addr
    
    def client_listener(self):

        while 7:
            try:
                data = self.Client.recv(3_000_000)
            except (ConnectionResetError, ConnectionAbortedError, OSError):
                self._client_lost()
                self.Server.close()
                break

            if len(data) < 1:
                self._client_lost()
                self.Server.close()
                break
                
            hr = self._from_client(data)
            if hr is None:
                continue
            try:
                self.Server.sendall(hr)
            except (ConnectionResetError, ConnectionAbortedError):
               self._server_lost()
    
    def server_listener(self):

        while 7:
            try:
                data = self.Server.recv(3_000_000)
            except (ConnectionResetError, ConnectionAbortedError, OSError):
                self._server_lost()
                self.Client.close()
                break

            if len(data) < 1:
                self._server_lost()
                self.Client.close()
                break
                
            hr = self._from_server(data)
            if hr is None:
                continue        
            try:
                self.Client.sendall(hr)
            except (ConnectionResetError, ConnectionAbortedError):
                self._client_lost()
    
    def asyncaccept(self):

        self.ClientFactory.setblocking(0)
        while 7:
            try:
                try:
                    self.Client, addr = self.ClientFactory.accept()
                    break
                except BlockingIOError:
                    time.sleep(0.07)
            except KeyboardInterrupt:
                exit()
        
        self.ClientFactory.setblocking(1)
        self.Client.setblocking(1)
    
    def join(self):

        while 7:
            self._waiting_for_client()
            self.asyncaccept()
            self._new_client()
            self.Server = socket.socket(2, 1)
            try:
                self.Server.connect(self.UpstreamAddr)
            except Exception as e:
                self._server_error(e)
                self.Client.close()
                continue
            self._new_server()      

            CT = threading.Thread(target=self.client_listener, daemon=True)
            ST = threading.Thread(target=self.server_listener, daemon=True)
            CT.start() ; ST.start()

            while CT.is_alive() or ST.is_alive():
                try:
                    time.sleep(0.178)
                except KeyboardInterrupt:                                        
                    return            
