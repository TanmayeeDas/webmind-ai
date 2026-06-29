from fastapi import APIRouter
from rag.chunker import chunk_text

router = APIRouter()


@router.get("/health")
def health():
    return {
        "status": "healthy"
    }


@router.post("/ask")
def ask(data: dict):

    chunks = chunk_text(data["page_text"])

    print("=" * 50)

    print("Total Chunks:", len(chunks))

    print("=" * 50)

    for i, chunk in enumerate(chunks):

        print(f"\nChunk {i+1}")

        print(chunk[:150])

    return {

        "answer": f"Successfully created {len(chunks)} chunks."

    }