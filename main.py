import os
from openai import OpenAI

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])


def fayez(message):
    response = client.responses.create(
        model="gpt-5.6-luna",
        input=message
    )
    return response.output_text


if __name__ == "__main__":
    print(fayez("مرحباً يا فايز، عرّف عن نفسك باختصار."))
