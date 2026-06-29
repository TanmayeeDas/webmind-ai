from openai import OpenAI
from dotenv import load_dotenv
import os

from prompts.prompt_template import SYSTEM_PROMPT

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)


def generate_answer(question: str, context: str):

    response = client.chat.completions.create(

        model="gpt-4.1-mini",

        temperature=0.2,

        messages=[

            {
                "role": "system",
                "content": SYSTEM_PROMPT
            },

            {
                "role": "user",
                "content":
                f"""
Context:

{context}


Question:

{question}
"""
            }

        ]

    )

    return response.choices[0].message.content