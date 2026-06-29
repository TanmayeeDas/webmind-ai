from fastapi import APIRouter
from rag.chunker import chunk_text
from rag.vector_store import create_vector_store

router = APIRouter()


@router.get("/health")
def health():
    return {
        "status": "healthy"
    }


@router.post("/index-page")
def index_page(data: dict):

    page_text = data["page_text"]

    chunks = chunk_text(page_text)

    print(f"Created {len(chunks)} chunks")

    vector_store = create_vector_store(chunks)

    print("Vector Store Created Successfully!")

    return {

        "message": "Page indexed successfully.",

        "chunks": len(chunks)

    }