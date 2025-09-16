# examples/sentence_test.py

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from opennlp_grpc.sentence_detector import SentenceDetectorClient

client = SentenceDetectorClient()

text = "Hello there. How are you doing today? I hope everything is fine."
sentences = client.detect(text)

print("Detected Sentences:")
for sentence in sentences:
    print(f"- {sentence}")
