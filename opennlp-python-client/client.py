# client.py
import grpc
from opennlp_grpc import opennlp_pb2, opennlp_pb2_grpc

def run():
    # connect to server
    channel = grpc.insecure_channel("localhost:50051")
    stub = opennlp_pb2_grpc.TokenizerTaggerServiceStub(channel)

    # make request
    request = opennlp_pb2.TokenizeRequest(sentence="Hello world from OpenNLP!")
    response = stub.Tokenize(request)

    print("Tokens:", response.values)

if __name__ == "__main__":
    run()
