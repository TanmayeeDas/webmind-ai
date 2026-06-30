



# from langchain_community.vectorstores import FAISS
# from rag.embeddings import embedding_model

# # Global variable to hold the current page's FAISS index
# vector_store = None


# def create_vector_store(chunks):
#     """
#     Creates a FAISS vector store from webpage chunks
#     and stores it in memory.
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


# # next part
# from langchain_community.vectorstores import FAISS
# from langchain_core.documents import Document

# from rag.embeddings import embedding_model

# # Global variable to hold the current page's FAISS index
# vector_store = None


# def create_vector_store(chunks, title="", url=""):

#     global vector_store

#     documents = []

#     for i, chunk in enumerate(chunks):

#         documents.append(

#             Document(

#                 page_content=chunk,

#                 metadata={

#                     "chunk_id": i + 1,
#                     "title": title,
#                     "url": url

#                 }

#             )

#         )

#     vector_store = FAISS.from_documents(

#         documents=documents,

#         embedding=embedding_model

#     )

#     return vector_store


# def get_vector_store():

#     return vector_store

from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document

from rag.embeddings import embedding_model

# Global objects
vector_store = None
documents = []
current_url = None


def create_vector_store(chunks, title="", url=""):

    global vector_store
    global documents
    global current_url

    documents = []

    for i, chunk in enumerate(chunks):

        documents.append(

            Document(

                page_content=chunk,

                metadata={

                    "chunk_id": i + 1,
                    "title": title,
                    "url": url

                }

            )

        )

    vector_store = FAISS.from_documents(

        documents,

        embedding_model

    )

    current_url = url
    return vector_store


def get_vector_store():

    return vector_store


def get_documents():

    return documents

def get_current_url():

    return current_url