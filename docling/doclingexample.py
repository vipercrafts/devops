import logging
logging.disable(logging.CRITICAL)
from docling.document_converter import DocumentConverter
from pathlib import Path



def parse_document(file_path: str):
    converter = DocumentConverter()

    # Convert to absolute path
    file_path = Path(file_path).resolve()

    if not file_path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")

    result = converter.convert(str(file_path))

    return {
        "markdown": result.document.export_to_markdown(),
        "text": result.document.export_to_text()
    }


if __name__ == "__main__":
    file_path = r"C:\Users\RAKESH\Desktop\viperCrafts\devops\docling\html_mcqs.pdf"
    output = parse_document(file_path)

    print(output["markdown"])
