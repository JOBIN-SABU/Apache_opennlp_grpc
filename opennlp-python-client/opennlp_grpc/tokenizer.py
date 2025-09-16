# opennlp_grpc/tokenizer.py

import grpc
from opennlp_grpc import opennlp_pb2, opennlp_pb2_grpc

class TokenizerClient:
    def __init__(self, host='localhost', port=50051, model_hash='en-token'):
        self.channel = grpc.insecure_channel(f"{host}:{port}")
        self.stub = opennlp_pb2_grpc.TokenizerTaggerServiceStub(self.channel)
        self.model_hash = model_hash

    def tokenize(self, text: str) -> list[str]:
        request = opennlp_pb2.TokenizeRequest(
            sentence=text,
            model_hash=self.model_hash
        )
        response = self.stub.Tokenize(request)  # Correct method name with a capital 'T'
        return list(response.tokens)
