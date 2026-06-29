from fastapi import APIRouter
from rag.chunker import chunk_text
from rag.vector_store import create_vector_store

router = APIRouter()


@router.get("/health")
def health():
    return {
        "status": "healthy"
    }


@router.post("/ask")
def ask(data: dict):

    #Step 1: Chunking
    chunks = chunk_text(data["page_text"])

    print("=" * 50)

    print("Total Chunks:", len(chunks))

    print("=" * 50)

    #Step 2: Print the first few chunks
    for i, chunk in enumerate(chunks):

        print(f"\nChunk {i+1}")

        print(chunk[:150])
    
    #Step 3: Create FAISS
    vector_store = create_vector_store(chunks)

    print("\n✅ Vector Store Created Successfully!")
    # Step 4 - Return response
    return {

        "answer": f"Vector Store Created Successfully with {len(chunks)} chunks."

    }

