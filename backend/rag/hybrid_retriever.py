from langchain_community.retrievers import BM25Retriever
from langchain.retrievers import EnsembleRetriever

from rag.vector_store import (
    get_vector_store,
    get_documents
)

from config import TOP_K


def hybrid_retrieve(question: str):

    vector_store = get_vector_store()
    documents = get_documents()

    if vector_store is None:
        raise ValueError("No page has been indexed.")

    if not documents:
        raise ValueError("No documents available.")

    # FAISS Retriever
    faiss_retriever = vector_store.as_retriever(

        search_kwargs={
            "k": TOP_K
        }

    )

    # BM25 Retriever
    bm25_retriever = BM25Retriever.from_documents(
        documents
    )

    bm25_retriever.k = TOP_K

    # Hybrid Retriever
    ensemble_retriever = EnsembleRetriever(

        retrievers=[
            faiss_retriever,
            bm25_retriever
        ],

        weights=[
            0.8,
            0.2
        ]

    )

    docs = ensemble_retriever.invoke(question)

    return docs