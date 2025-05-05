import chromadb

# Use the same persistent client path as before
client = chromadb.PersistentClient(path="./chroma_db")

# Get your collection
collection = client.get_or_create_collection(name="documents")

# Get documents and metadata (IDs are returned automatically)
results = collection.get(include=["documents", "metadatas"])

# Print out each chunk's metadata and a preview
for i, (doc, meta, doc_id) in enumerate(zip(results["documents"], results["metadatas"], results["ids"])):
    print(f"\nChunk {i + 1} (ID: {doc_id}):")
    print("Metadata:", meta)
    print("Text preview:", doc[:150], "...\n")  # Only previewing first 150 characters




# With runnnig this file you will be able to inspect the what's stored in ChromaDB
# Each stored chunk of text.
# The associated section metadata (like "Introduction", "Methods", etc.).