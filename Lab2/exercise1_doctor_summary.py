from groq import Groq
import os
from dotenv import load_dotenv
load_dotenv()
key = os.getenv("GROQ_API_KEY")
client = Groq(api_key=key)

def ask_llm(system_prompt,user_prompt):
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role":"system",
                "content":system_prompt
            },
            {
                "role": "user",
                "content": user_prompt,
            }
        ],

        # The language model which will generate the completion.
        model="openai/gpt-oss-120b"
    )
    response = chat_completion.choices[0].message.content

    return response

system_prompt = "You are an Doctor. You will get paitent's notes and name your task is to generate a clean doctor summary. " \
"The summary with fixed sections - Name of Paitent,Symptoms,Diagonosis,Recommendation - in same format every time, regardless of input.In case of unrelated or invalid input just specify your role dont output any summary"

user_prompt = """My name is {name} and i have {notes}"""

print(ask_llm(system_prompt,user_prompt.format(name="Raj",notes="I have cold and cough")))

query = "How are you"

print(ask_llm(system_prompt,query))
