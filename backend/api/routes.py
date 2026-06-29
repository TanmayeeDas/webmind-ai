# from fastapi import APIRouter
# from rag.chunker import chunk_text
# from rag.vector_store import create_vector_store
# from rag.retriever import retrieve_context

# router = APIRouter()


# @router.get("/health")
# def health():
#     return {
#         "status": "healthy"
#     }


# @router.post("/index-page")
# def index_page(data: dict):

#     page_text = data["page_text"]

#     chunks = chunk_text(page_text)

#     print(f"Created {len(chunks)} chunks")

#     vector_store = create_vector_store(chunks)

#     print("Vector Store Created Successfully!")

#     return {

#         "message": "Page indexed successfully.",

#         "chunks": len(chunks)

#     }

# @router.post("/retrieve")
# def retrieve(data: dict):

#     # page_text = data["page_text"]

#     question = data["question"]

#     # chunks = chunk_text(page_text)

#     # vector_store = create_vector_store(chunks)

#     docs = retrieve_context(

#         # vector_store,

#         question

#     )

#     print("="*50)

#     print("Retrieved Chunks")

#     print("="*50)

#     for i, doc in enumerate(docs):

#         print()

#         print(f"Chunk {i+1}")

#         print(doc.page_content[:200])

#     return{

#         "answer":"Retrieval Successful!"

#     }


from fastapi import APIRouter

from rag.chunker import chunk_text
from rag.vector_store import create_vector_store
from rag.retriever import retrieve_context
from services.openai_service import generate_answer

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

    print("=" * 50)
    print("Page Indexing Started")
    print("=" * 50)

    print(f"Chunks Created : {len(chunks)}")

    create_vector_store(chunks)

    print("FAISS Index Created Successfully!")

    return {
        "message": "Page indexed successfully.",
        "chunks": len(chunks)
    }


@router.post("/retrieve")
def retrieve(data: dict):

    question = data["question"]

    docs = retrieve_context(question)

    print("=" * 50)
    print("Retrieved Chunks")
    print("=" * 50)

    context = ""

    for i, doc in enumerate(docs):

        print(f"\nChunk {i+1}\n")

        print(doc.page_content[:200])

        context += doc.page_content + "\n\n"

    answer = generate_answer(
        question=question,
        context=context
    )

    return {

        "answer": answer

    }