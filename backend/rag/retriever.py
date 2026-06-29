


# from rag.vector_store import get_vector_store


# def retrieve_context(question: str):

#     """
#     Retrieve the most relevant chunks
#     from the current webpage.
#     """

#     vector_store = get_vector_store()

#     if vector_store is None:
#         raise ValueError("No page has been indexed yet.")

#     retriever = vector_store.as_retriever(

#         search_kwargs={
#             "k": 4
#         }

#     )

#     docs = retriever.invoke(question)

#     return docs

from rag.vector_store import get_vector_store
from config import TOP_K


def retrieve_context(question: str):

    vector_store = get_vector_store()

    if vector_store is None:
        raise ValueError("No page has been indexed yet.")

    results = vector_store.similarity_search_with_score(

        query=question,

        k=TOP_K

    )

    return results