# module_python

![basic-test](https://github.com/molabokchi/module_python/workflows/basic-test/badge.svg)

module python library

# Requirement Installation

```console
python3 -m pip install -r requirements.txt
```

# Generate Python GRPC files from Proto

Type the following at the root
```console
python3 -m grpc_tools.protoc -I. --python_out=. --pyi_out=. --grpc_python_out=. deepdriver/sdk/interface/grpc_interface.proto
```
