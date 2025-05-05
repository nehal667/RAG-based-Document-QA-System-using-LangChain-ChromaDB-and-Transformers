# # vector_store.py
# from sentence_transformers import SentenceTransformer
# import chromadb

# class VectorStore:
#     def __init__(self):
#         self.client = chromadb.PersistentClient(path="./chroma_db")
#         self.collection = self.client.get_or_create_collection(name="documents")
#         self.embedder = SentenceTransformer('all-MiniLM-L6-v2')

#     def add(self, chunks, metadatas):
#         embeddings = self.embedder.encode(chunks).tolist()
#         for i, (chunk, meta, emb) in enumerate(zip(chunks, metadatas, embeddings)):
#             self.collection.add(
#                 documents=[chunk],
#                 ids=[f"chunk_{i}"],
#                 embeddings=[emb],
#                 metadatas=[meta]
#             )
# vector_store.py
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings

class VectorStore:
    def __init__(self, persist_directory="./chroma_db"):
        self.persist_directory = persist_directory
        self.embedding_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
        self.vectordb = Chroma(
            persist_directory=self.persist_directory,
            embedding_function=self.embedding_model
        )

    def add(self, texts, metadatas):
        self.vectordb.add_texts(texts=texts, metadatas=metadatas)
        self.vectordb.persist()

    def get_retriever(self, k=3, metadata_filter=None):
        return self.vectordb.as_retriever(search_kwargs={"k": k, "filter": metadata_filter})
