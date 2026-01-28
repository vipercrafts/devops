import sys
sys.stdout.reconfigure(encoding="utf-8")

import logging
logging.disable(logging.CRITICAL)

import gdown
from docling.document_converter import DocumentConverter
from pathlib import Path

def parse_google_drive_file(drive_url: str):
    output_file = "downloaded.pdf"

    gdown.download(
        url=drive_url,
        output=output_file,
        quiet=True,
        fuzzy=True   # 🔥 IMPORTANT
    )

    file_path = Path(output_file).resolve()
    if not file_path.exists():
        raise FileNotFoundError("Download failed")

    converter = DocumentConverter()
    result = converter.convert(str(file_path))

    return result.document.export_to_text()


if __name__ == "__main__":
    drive_link = "https://drive.google.com/file/d/1E7Kz1icPT_jMmtMSE2aRemF4ulOvWRB0bvxYR4Hv1Tc/view"
    text = parse_google_drive_file(drive_link)

    print(text)
