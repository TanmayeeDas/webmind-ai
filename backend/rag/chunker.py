from langchain_text_splitters import RecursiveCharacterTextSplitter


def chunk_text(page_text: str):

    splitter = RecursiveCharacterTextSplitter(

        chunk_size=1000,

        chunk_overlap=200,

        separators=[
            "\n\n",
            "\n",
            ". ",
            " ",
            ""
        ]

    )

    chunks = splitter.split_text(page_text)

    return chunks