import grpc
from concurrent import futures
import time

# 👇 absolute imports instead of relative
from opennlp_grpc import opennlp_pb2, opennlp_pb2_grpc


class TokenizerTaggerService(opennlp_pb2_grpc.TokenizerTaggerServiceServicer):
    def Tokenize(self, request, context):
        text = request.sentence
        tokens = text.split()
        return opennlp_pb2.StringList(values=tokens)



def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    opennlp_pb2_grpc.add_TokenizerTaggerServiceServicer_to_server(
        TokenizerTaggerService(), server
    )
    server.add_insecure_port("[::]:50051")
    server.start()
    print("✅ gRPC Server started on port 50051...")
    try:
        while True:
            time.sleep(86400)
    except KeyboardInterrupt:
        server.stop(0)



if __name__ == "__main__":
    serve()
