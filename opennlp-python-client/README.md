# OpenNLP gRPC Prototype (Minimal)

This is a minimal proof-of-concept gRPC wrapper for Apache OpenNLP to expose its tokenization functionality as a remote service.

## Requirements
- Python 3.8+
- Java 11+
- Apache OpenNLP 2.5.5 installed and accessible via `./bin/opennlp`
- Install Python dependencies:
- pip install -r requirements.txt


## Usage

### 1. Start the gRPC server
- cd opennlp-grpc
- python -m opennlp_grpc.server


### 2. Run the client
- cd opennlp-grpc/examples
- python tokenizer_test.py "This is a test sentence."


### 3. Expected Output
- Tokens: ['This', 'is', 'a', 'test', 'sentence', '.']


### Notes
- This is **minimal**: only `SimpleTokenizer` is supported.
- Next steps: expand to POS tagging, sentence detection, etc.,     based on Apache feedback.
