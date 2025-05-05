# rag_query.py
# With this file you can ask query and based on the information stored in the chromadb it will
# provide you with the answer
from vector_store import VectorStore
from transformers import pipeline

def get_context(query: str, section_filter: str = None, k: int = 3):
    store = VectorStore()
    
    filter_dict = {"section": section_filter} if section_filter else None
    retriever = store.get_retriever(k=k, metadata_filter=filter_dict)
    
    docs = retriever.get_relevant_documents(query)
    return " ".join([doc.page_content for doc in docs])

def main():
    qa_pipeline = pipeline("text2text-generation", model="google/flan-t5-base")

    query = input("Ask a question: ")
    section = input("Filter by section (optional, e.g., 'Introduction'): ").strip() or None

    context = get_context(query, section_filter=section)
    prompt = f"Answer the question using the context: {context}\nQuestion: {query}"
    response = qa_pipeline(prompt)

    print("\nAnswer:", response[0]['generated_text'])

if __name__ == "__main__":
    main()
