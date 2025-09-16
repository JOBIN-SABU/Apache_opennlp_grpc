# opennlp_grpc/sentence_detector.py

import grpc
from opennlp_grpc import opennlp_pb2, opennlp_pb2_grpc

class SentenceDetectorClient:
    def __init__(self, host='localhost', port=50051, model_hash='en-sent'):
        self.channel = grpc.insecure_channel(f"{host}:{port}")
        self.stub = opennlp_pb2_grpc.SentenceDetectorServiceStub(self.channel)
        self.model_hash = model_hash

    def detect(self, text: str) -> list[str]:
        request = opennlp_pb2.SentDetectRequest(
            sentence=text,
            model_hash=self.model_hash
        )
        response = self.stub.sentDetect(request)
        return list(response.values)
