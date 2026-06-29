# def retrieve_context(vector_store, question):

#     retriever = vector_store.as_retriever(

#         search_kwargs={

#             "k":4

#         }

#     )

#     docs = retriever.invoke(question)

#     return docs


from rag.vector_store import get_vector_store


def retrieve_context(question: str):

    """
    Retrieve the most relevant chunks
    from the current webpage.
    """

    vector_store = get_vector_store()

    if vector_store is None:
        raise ValueError("No page has been indexed yet.")

    retriever = vector_store.as_retriever(

        search_kwargs={
            "k": 4
        }

    )

    docs = retriever.invoke(question)

    return docs