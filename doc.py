import sys
import os

class SuppressStdout:
    def __enter__(self):
        self._stdout = sys.stdout
        sys.stdout = open(os.devnull, 'w')

    def __exit__(self, exc_type, exc_val, exc_tb):
        sys.stdout.close()
        sys.stdout = self._stdout

from docling.document_converter import DocumentConverter
import json

with SuppressStdout():
    converter = DocumentConverter()
    result = converter.convert("https://arxiv.org/pdf/2408.09869")

print(json.dumps(result.document.export_to_dict(), indent=2))
