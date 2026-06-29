from fastapi import APIRouter

from rag.chunker import chunk_text
from rag.vector_store import create_vector_store
# from rag.retriever import retrieve_context
from rag.hybrid_retriever import hybrid_retrieve
from services.openai_service import generate_answer
from models.request import IndexPageRequest
from models.request import RetrieveRequest

from config import SIMILARITY_THRESHOLD

router = APIRouter()


@router.get("/health")
def health():
    return {
        "status": "healthy"
    }


@router.post("/index-page")
def index_page(data: IndexPageRequest):

    try:

        page_text = data.page_text.strip()

        if not page_text:

            return {

                "message": "This page contains no readable content.",

                "chunks": 0

            }

        chunks = chunk_text(page_text)

        if not chunks:

            return {

                "message": "Failed to create chunks.",

                "chunks": 0

            }

        print("=" * 50)
        print("Page Indexing Started")
        print("=" * 50)

        print(f"Page Title : {data.page_title}")
        print(f"Chunks Created : {len(chunks)}")

        create_vector_store(

            chunks,

            title=data.page_title,

            url=data.page_url

        )

        print("FAISS Index Created Successfully!")

        return {

            "message": "Page indexed successfully.",

            "chunks": len(chunks)

        }

    except Exception as e:

        print(f"\nIndexing Error : {e}")

        return {

            "message": "Failed to index the webpage.",

            "chunks": 0

        }

@router.post("/retrieve")
def retrieve(data: RetrieveRequest):

    try:

        question = data.question.strip()

        if not question:

            return {

                "answer": "Please enter a valid question."

            }

        # results = retrieve_context(question)
        docs = hybrid_retrieve(question)

        if not docs:

            return {

                "answer": "I couldn't find the answer on this webpage."

            }

        # best_score = results[0][1]

        # print(f"\nBest Score : {best_score:.4f}")


        # if best_score > SIMILARITY_THRESHOLD:

        #     return {

        #         "answer": "I couldn't find the answer on this webpage."

        #     }

        print("=" * 50)
        print("Retrieved Chunks")
        print("=" * 50)

        context = ""

        for i, doc in enumerate(docs):

            print(f"\nChunk {i+1}")

            print(doc.page_content[:200])

            context += doc.page_content + "\n\n"

        answer = generate_answer(

            question=question,

            context=context

        )

        return {

            "answer": answer,

        "sources": [

            {

                "chunk": doc.metadata["chunk_id"],

                "title": doc.metadata["title"]

            }

            for doc in docs

        ]

        }

    except Exception as e:

        print(f"\nRetrieve Error : {e}")

        return {

            "answer": "Something went wrong while processing your request."

        }