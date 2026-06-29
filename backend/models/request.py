from pydantic import BaseModel


class IndexPageRequest(BaseModel):

    page_title: str
    page_url: str
    page_text: str


class RetrieveRequest(BaseModel):

    question: str