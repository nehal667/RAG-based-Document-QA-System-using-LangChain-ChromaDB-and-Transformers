# import gradio as gr
# from sentence_transformers import SentenceTransformer
# import chromadb
# from transformers import pipeline

# # Initialize models and ChromaDB
# embedder = SentenceTransformer('all-MiniLM-L6-v2')
# client = chromadb.PersistentClient(path="./chroma_db")
# collection = client.get_or_create_collection(name="documents")
# qa_pipeline = pipeline("text2text-generation", model="google/flan-t5-base")

# def answer_question(query, section_filter=""):
#     query_embedding = embedder.encode(query).tolist()

#     # Query with optional metadata filter
#     if section_filter.strip():
#         results = collection.query(query_embeddings=[query_embedding], n_results=3, where={"section": section_filter})
#     else:
#         results = collection.query(query_embeddings=[query_embedding], n_results=3)

#     if not results["documents"]:
#         return "No matching context found."

#     context = " ".join([doc for docs in results["documents"] for doc in docs])
#     prompt = f"""Use the following context to answer the question.
#     Context: {context}
#     Question: {query}
#     Answer:"""
#     response = qa_pipeline(prompt)

#     return response[0]['generated_text']

# # Gradio UI
# iface = gr.Interface(
#     fn=answer_question,
#     inputs=[
#         gr.Textbox(label="Ask a Question"),
#         gr.Textbox(label="Filter by Section (optional)")
#     ],
#     outputs="text",
#     title="Document QA with RAG",
#     description="Ask questions based on uploaded documents. Uses ChromaDB and Transformers."
# )

# iface.launch()
