import os
from PyPDF2 import PdfReader
import docx2txt

class DocumentLoader:
    def __init__(self, path):
        self.path = path

    def load(self):
        ext = os.path.splitext(self.path)[1].lower()

        if ext == ".pdf":
            return self._load_pdf()
        elif ext == ".docx":
            return self._load_docx()
        else:
            raise ValueError("Unsupported file type. Only .pdf and .docx are supported.")

    def _load_pdf(self):
        try:
            reader = PdfReader(self.path)
            text = ""
            for page in reader.pages:
                text += page.extract_text()
            return text
        except Exception as e:
            print(f"Error reading PDF: {e}")
            return None

    def _load_docx(self):
        try:
            return docx2txt.process(self.path)
        except Exception as e:
            print(f"Error reading DOCX: {e}")
            return None
