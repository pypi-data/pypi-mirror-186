from __future__ import annotations
import asyncio
import threading
import websockets
from concurrent.futures import Future
from google.protobuf.message import Message
from typing import Dict, Any, Tuple, Callable
from google.protobuf.descriptor import MethodDescriptor
from google.protobuf.service import Service, RpcChannel, RpcController

from . import meta_pb2

class WebSocketRpcServer(threading.Thread):
    def __init__(self, host, port):
        super().__init__()
        self.host = host
        self.port = port
        self.ws = None
        self.handlers: Dict[str, Tuple[type[Message], type[Message], Callable]] = {}
        self.loop = asyncio.new_event_loop()
        self.run = self.loop.run_forever
        self.daemon = True
    def start(self, block=True) -> None:
        super().start()
        future = asyncio.run_coroutine_threadsafe(self._start(), self.loop)
        if block:
            while not future.done(): pass
    async def _start(self):
        await websockets.serve(self._run, self.host, self.port)
        await asyncio.Future()
    async def _run(self, websocket, path):
        try:
            async for message in websocket:
                meta_request = meta_pb2.MetaRequest.FromString(message)
                for full_name in self.handlers.keys():
                    if meta_request.full_name == full_name:
                        request_class, response_class, handler = self.handlers[full_name]
                        request = request_class.FromString(meta_request.request)
                        res = handler({field.name: value for field, value in request.ListFields()})
                        response = response_class(**res)
                        meta_response = meta_pb2.MetaResponse(full_name=full_name, response=response.SerializeToString())
                        data = meta_response.SerializeToString()
                        await websocket.send(data)
        except websockets.exceptions.ConnectionClosedError:
            pass
    def add_handler(self, full_name, request_class, response_class, handler):
        self.handlers[full_name] = (request_class, response_class, handler)

class WebSocketRpcChannel(RpcChannel, threading.Thread):
    def __init__(self, url) -> None:
        super().__init__()
        self.url = url
        self.ws = None
        self.loop = asyncio.new_event_loop()
        self.run = self.loop.run_forever
        self.daemon = True
        self.start()
    async def _CallMethod(self, method_descriptor: MethodDescriptor, rpc_controller: RpcController, request: Message, response_class: type[Message], done: Callable[[Message], None] | None) -> Future[Message] | None:
        if self.ws is None:
            self.ws = await websockets.connect(self.url)
        meta_request = meta_pb2.MetaRequest(full_name=method_descriptor.full_name, request=request.SerializeToString())
        data = meta_request.SerializeToString()
        await self.ws.send(data)
        data = await self.ws.recv()
        meta_response = meta_pb2.MetaResponse.FromString(data)
        response = response_class.FromString(meta_response.response)
        return {field.name: value for field, value in response.ListFields()}
    def CallMethod(self, method_descriptor: MethodDescriptor, rpc_controller: RpcController, request: Message, response_class: type[Message], done: Callable[[Message], None] | None) -> Future[Message] | None:
        future = asyncio.run_coroutine_threadsafe(self._CallMethod(method_descriptor, rpc_controller, request, response_class, done), self.loop)
        return future.result()
    def __del__(self):
        self.loop.close()

class WebSocketRpcController(RpcController):
    pass

class WebSocketRpcMethodClient:
    def __init__(self, service_client: WebSocketRpcServiceClient, name, request_class: type[Message], response_class: type[Message]) -> None:
        self.service_client = service_client
        self.name = name
        self.request_class = request_class
        self.response_class = response_class
    def call(self, **kwargs) -> Dict[str, Any]:
        res = getattr(self.service_client.stub, self.name)(self.service_client.wrpc_client.controller, self.request_class(**kwargs), None)
        return res

class WebSocketRpcServiceClient:
    def __init__(self, wrpc_client: WebSocketRpcClient, stub_class: type[Service]) -> None:
        self.wrpc_client = wrpc_client
        self.stub = stub_class(self.wrpc_client.channel)
    def method(self, name, request_class: type[Message], response_class: type[Message]) -> WebSocketRpcMethodClient:
        return WebSocketRpcMethodClient(self, name, request_class, response_class)

class WebSocketRpcClient:
    def __init__(self, url) -> None:
        self.channel = WebSocketRpcChannel(url)
        self.controller = WebSocketRpcController()
    def service(self, stub_class: type[Service]) -> WebSocketRpcServiceClient:
        return WebSocketRpcServiceClient(self, stub_class)