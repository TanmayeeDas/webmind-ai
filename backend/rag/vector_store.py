from langchain_community.vectorstores import FAISS

from rag.embeddings import embedding_model


def create_vector_store(chunks):

    vector_store = FAISS.from_texts(

        texts=chunks,

        embedding=embedding_model

    )

    return vector_store