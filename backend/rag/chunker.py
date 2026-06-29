# from langchain_text_splitters import RecursiveCharacterTextSplitter
# from config import CHUNK_SIZE, CHUNK_OVERLAP

# def chunk_text(page_text: str):

#     splitter = RecursiveCharacterTextSplitter(

#         chunk_size=CHUNK_SIZE,

#         chunk_overlap=CHUNK_OVERLAP,

#         separators=[
#             "\n\n",
#             "\n",
#             ". ",
#             " ",
#             ""
#         ]

#     )

#     chunks = splitter.split_text(page_text)

#     return chunks

from langchain_text_splitters import RecursiveCharacterTextSplitter

from config import (
    CHUNK_SIZE,
    CHUNK_OVERLAP
)


def chunk_text(page_text: str):

    splitter = RecursiveCharacterTextSplitter(

        chunk_size=CHUNK_SIZE,

        chunk_overlap=CHUNK_OVERLAP,

        separators=[

            "\n# ",

            "\n## ",

            "\n### ",

            "\n\n",

            "\n",

            ". ",

            "? ",

            "! ",

            "; ",

            ", ",

            " ",

            ""

        ]

    )

    return splitter.split_text(page_text)