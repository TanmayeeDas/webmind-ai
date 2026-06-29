# from openai import OpenAI
# from dotenv import load_dotenv
# import os

# from prompts.prompt_template import SYSTEM_PROMPT

# load_dotenv()

# client = OpenAI(
#     api_key=os.getenv("OPENAI_API_KEY")
# )


# def generate_answer(question: str, context: str):

#     response = client.chat.completions.create(

#         model="gpt-4.1-mini",

#         temperature=0.2,

#         messages=[

#             {
#                 "role": "system",
#                 "content": SYSTEM_PROMPT
#             },

#             {
#                 "role": "user",
#                 "content":
#                 f"""
# Context:

# {context}


# Question:

# {question}
# """
#             }

#         ]

#     )

#     return response.choices[0].message.content

from openai import OpenAI
from dotenv import load_dotenv
import os

from prompts.prompt_template import SYSTEM_PROMPT
from config import MODEL_NAME, TEMPERATURE

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("OPENAI_API_KEY not found in .env file.")

client = OpenAI(api_key=api_key)


def generate_answer(question: str, context: str):

    try:

        response = client.chat.completions.create(

            model=MODEL_NAME,

            temperature=TEMPERATURE,

            messages=[

                {
                    "role": "system",
                    "content": SYSTEM_PROMPT
                },

                {
                    "role": "user",
                    "content": f"""
Context:

{context}


Question:

{question}
"""
                }

            ]

        )

        return response.choices[0].message.content

    except Exception as e:

        print(f"\nOpenAI Error: {e}")

        return (
            "Sorry, I couldn't generate an answer right now. "
            "Please try again later."
        )