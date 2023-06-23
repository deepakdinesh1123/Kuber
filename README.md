# Kuber
python -m grpc_tools.protoc -I./protos/ --python_out=. --pyi_out=. --grpc_python_out=. protos/definitions/execute.proto


protoc -I=./protos environment.proto \
    --js_out=import_style=commonjs:ui/grpc-client/environment \
    --grpc-web_out=import_style=commonjs,mode=grpcwebtext:ui/grpc-client/environment
