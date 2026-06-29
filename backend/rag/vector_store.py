# from langchain_community.vectorstores import FAISS
# from rag.embeddings import embedding_model

# # Global variable
# vector_store = None


# def create_vector_store(chunks):
#     """
#     Creates a FAISS vector store and saves it globally.
#     """

#     global vector_store

#     vector_store = FAISS.from_texts(
#         texts=chunks,
#         embedding=embedding_model
#     )

#     return vector_store


# def get_vector_store():
#     """
#     Returns the current FAISS vector store.
#     """

#     return vector_store




from langchain_community.vectorstores import FAISS
from rag.embeddings import embedding_model

# Global variable to hold the current page's FAISS index
vector_store = None


def create_vector_store(chunks):
    """
    Creates a FAISS vector store from webpage chunks
    and stores it in memory.
    """

    global vector_store

    vector_store = FAISS.from_texts(
        texts=chunks,
        embedding=embedding_model
    )

    return vector_store


def get_vector_store():
    """
    Returns the current FAISS vector store.
    """

    return vector_store