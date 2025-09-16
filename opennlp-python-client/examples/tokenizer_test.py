# examples/tokenizer_test.py
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'opennlp_grpc')))

from opennlp_grpc.tokenizer import TokenizerClient

client = TokenizerClient()

text = "Hello"
tokens = client.tokenize(text)

print("Tokens:")
for token in tokens:
    print(f"- {token}")
