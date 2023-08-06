# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['wrpc']

package_data = \
{'': ['*']}

install_requires = \
['protobuf>=4.21.12,<5.0.0', 'websockets>=10.4,<11.0']

setup_kwargs = {
    'name': 'websocket-rpcs',
    'version': '0.1.0',
    'description': 'rpc over websocket uses protobuf to serialize data',
    'long_description': 'rpc over websocket uses protobuf to serialize data\n\n## Prepare\n\n### install package\n```bash\npip install websocket-rpcs\n```\n\n### write proto file (math.proto)\n```proto\nsyntax = "proto3";\n\noption py_generic_services = true;\n\nmessage SumArg {\n    int32 a = 1;\n    int32 b = 2;\n}\n\nmessage SumResult {\n    int32 sum = 1;\n}\n\nservice Math {\n    rpc Sum(SumArg) returns (SumResult);\n}\n```\n\n### generate python file (math_pb2.py math_pb2.pyi)\n```bash\nprotoc --python_out=. --pyi_out=. math.proto\n```\n\n## Example\n\n### Server\n\n```python\nimport wrpc\nimport math_pb2\ndef sum(args):\n    return {\n        "sum": args["a"] + args["b"]\n    }\nwrpc_server = wrpc.WebSocketRPCServer("0.0.0.0", 5887)\nwrpc_server.add_handler("Math.Sum", sum_pb2.SumArg,sum_pb2.SumResult, sum)\nwrpc_server.start()\n```\n\n### Client\n\n```python\nimport wrpc\nimport math_pb2\nwrpc_client = wrpc.WebSocketRpcClient("ws://localhost:5887")\nsum_client = wrpc_client.init(sum_pb2.Sum_Stub, sum_pb2.SumArg, sum_pb2.SumResult)\nres = sum_client.call("Sum", a=1, b=2)\n```',
    'author': 'jawide',
    'author_email': 'jawide@qq.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
