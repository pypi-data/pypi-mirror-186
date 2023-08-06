"""
    MineCraft Rewrite Proxy
    =======================
"""

import traceback
from .jnlog import CustomFormatter
import logging
from importlib import import_module
from unittest.mock import MagicMock
from time import sleep

import cubelib
import MCRP

from .tcproxy import tcproxy

Relative = MagicMock()

class MCRewriteProxy(tcproxy):    

    ServerBoundBuff = [b""] # it's a little trick to make immutable type (bytes)
    ClientBoundBuff = [b""] # mutable to pass reference to it

    PROTOCOL = cubelib.proto
    STATE = cubelib.state.Handshaking
    COMPRESSION_THR = -1
    SKIP = False

    HANDLERS = {} # {cubelib.proto.v47.ServerBound.ChatMessage: [False, <function handler at 0x00000...>]}
    REL_HANDLERS = {}

    ServerBoundHandler = None
    ClientBoundHandler = None
    
    def __init__(self, listen_addr: tuple, upstream_addr: tuple, verbose=False):

        super().__init__(listen_addr, upstream_addr)
        self.logger = logging.getLogger("MCRP")
        self.logger.setLevel(logging.DEBUG if verbose else logging.INFO)        
        stdout_handler = logging.StreamHandler()
        stdout_handler.setLevel(logging.DEBUG)

        stdout_handler.setFormatter(CustomFormatter('[%(asctime)s] [%(name)s] [%(levelname)s] %(message)s'))
        self.logger.addHandler(stdout_handler)

        self.logger.info(f"Running MCRP v{MCRP.version} (cubelib version {cubelib.version})")
        self.logger.info(f"Proxying config is: \u001b[97m{':'.join([str(a) for a in listen_addr])} \u001b[92m-> \u001b[97m{':'.join([str(a) for a in upstream_addr])}")        

    def _waiting_for_client(self):
        
        print()
        self.logger.info(f"Waiting for client connection...")

    def _new_client(self):

        self.logger.info(f"New client, creating connection to the server")
            
    def _new_server(self):

        self.logger.info(f"Connected to the server")
        self.logger.info("Reseting state to Handshaking")
        self.STATE = cubelib.state.Handshaking
        self.PROTOCOL = cubelib.proto
        self.COMPRESSION_THR = -1

        # Remove relative handlers for old protocol
        for handler in dict(self.HANDLERS):
            if self.HANDLERS[handler][0] == True:
                del self.HANDLERS[handler]        
    
    def _client_lost(self):

        self.logger.info(f"Client disconnected")
    
    def _server_lost(self):

        self.logger.info(f"Server disconnected")
    
    def _server_error(self, error):
        
        self.logger.error(f"Failed to connect to the server due to an error: {error}")
    
    def _from_client(self, data):

        return self._handle_bytes(data, self.ServerBoundBuff, cubelib.bound.Server)

    def _from_server(self, data):

        return self._handle_bytes(data, self.ClientBoundBuff, cubelib.bound.Client)

    def _handle_bytes(self, data, buff, bound):

        if self.SKIP:
            r = b""
            if buff[0]:
                r += buff[0]
                buff[0] = b""
            return r

        try:
            packs = []
            buff[0] += data
            buff[0] = cubelib.readPacketsStream(buff[0], self.COMPRESSION_THR, bound, packs)

            ret = b""
            for p in packs:
                try:
                    hr = self._handle_packet(p)
                    if isinstance(hr, bytes):
                        ret += hr
                    elif hr is False:
                        ret += b""
                    elif hr is None:
                        ret += p.build(self.COMPRESSION_THR if p.compressed else -1)
                    else:
                        ret += p.build(self.COMPRESSION_THR if p.compressed else -1)
                        self.logger.warn(f'обработчик сделал хуйню (вернул {hr})')                    

                except Exception as e:
                    self.logger.warn(f"Exception in {bound.name}Bound Handler: {e}")                    
                    self.logger.warn(traceback.format_exc())
                    ret += p.build(self.COMPRESSION_THR if p.compressed else -1)
            
            return ret

        except Exception as e:
            self.logger.error(f"Exception in {bound.name}Bound: {e}")
            self.logger.error(traceback.format_exc())

    def _handle_packet(self, pack):
        
        p = pack.resolve(self.STATE, self.PROTOCOL)
        t = p.__class__

        # Global bound handlers
        if pack.bound == cubelib.bound.Client:
            self.ClientBoundHandler(p) if self.ClientBoundHandler else None
        else:
            self.ServerBoundHandler(p) if self.ServerBoundHandler else None                

        # Handle handshake
        if t is cubelib.proto.ServerBound.Handshaking.Handshake:
            self._handle_handshake(p)

        if self.STATE is cubelib.state.Login:
            
            # Handle SetCompression
            if t is self.PROTOCOL.ClientBound.Login.SetCompression:
                self.logger.info(f"Point of switching-on compression with threshold {p.Threshold}")
                self.COMPRESSION_THR = p.Threshold

            # Handle LoginSuccess
            if t is self.PROTOCOL.ClientBound.Login.LoginSuccess:
                self.STATE = cubelib.state.Play
                self.logger.info(f"State changed to {self.STATE}")        

        # Call a handler if exists        
        return self.HANDLERS[t][1](p) if t in self.HANDLERS else None
        
    def _handle_handshake(self, p):

        if p.NextState == cubelib.NextState.Status:
            self.STATE = cubelib.state.Status
            return
        
        self.STATE = cubelib.state.Login
        self.logger.info(f"State changed to {self.STATE}, trying to load protocol v{p.ProtoVer}")
        if p.ProtoVer in cubelib.supported_versions:        
            self.PROTOCOL = import_module(f"cubelib.proto.v{p.ProtoVer}")
        else:
            self.logger.warn(f"Failed to load protocol v{p.ProtoVer}, looks like its unsupported! Enabling packet skip")
            self.SKIP = True

        self.logger.info(f"Successfuly loaded protovol v{p.ProtoVer}" + (f", trying to compile {len(self.REL_HANDLERS)} handlers..." if self.REL_HANDLERS else ""))

        for handler in self.REL_HANDLERS:            
            attrs = handler._extract_mock_name().split('.')[1:]
            obj = self.PROTOCOL
            for attr in attrs:
                obj = getattr(obj, attr, None)
                if not obj:
                    self.logger.warn(f'Failed to resolve handler {self.PROTOCOL.__name__}.{".".join(attrs)}')
                    break
            if obj:
                self.logger.debug(f"Successfully resolved {handler} into {obj}")
                self.HANDLERS[obj] = [True, self.REL_HANDLERS[handler]]

    def on(self, type_):
        def no(fun):
            if isinstance(type_, MagicMock):
                self.REL_HANDLERS[type_] = fun
            else:
                self.HANDLERS[type_] = [False, fun]
        return no
    
    def ClientBound(self, handler):
        self.ClientBoundHandler = handler
    
    def ServerBound(self, handler):
        self.ServerBoundHandler = handler

    def join(self):
        
        self.logger.info(f'Registred direct handlers list[{len(self.HANDLERS)}]:')
        for handler in self.HANDLERS:
            self.logger.info(f"    {handler}")

        self.logger.info(f'Registred relative handlers list[{len(self.REL_HANDLERS)}]:')
        for handler in self.REL_HANDLERS:
            self.logger.info(f"    {handler}")

        self.logger.debug('Entering mainloop')
        super().join()    
        p = self.PROTOCOL.ClientBound.Play.Disconnect('proxy_closed').build(self.COMPRESSION_THR)
        self.Client.send(p)
        self.logger.debug('Exiting')
