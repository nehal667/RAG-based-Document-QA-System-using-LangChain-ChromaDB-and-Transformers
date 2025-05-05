import os
from dotenv import load_dotenv
from document_loader import DocumentLoader
from chunker import Chunker
from classifier import SectionClassifier
from vector_store import VectorStore

load_dotenv()

def run_pipeline(folder_path):
    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)
        print(f"\nProcessing: {file_path}")

        try:
            loader = DocumentLoader(file_path)
            text = loader.load()
        except Exception as e:
            print(f"Error loading file: {e}")
            continue

        chunker = Chunker()
        chunks = chunker.chunk(text)

        classifier = SectionClassifier()
        metadatas = [{"section": classifier.classify(chunk)} for chunk in chunks]

        store = VectorStore()
        store.add(chunks, metadatas)
        print(f"Stored {len(chunks)} chunks from {file_name}.\n")

if __name__ == "__main__":
    run_pipeline("uploads")
