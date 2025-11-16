# To run this code you need to install the following dependencies:
# pip install google-genai

import base64
import os
from google import genai
from google.genai import types


def generate():
    client = genai.Client(
        api_key="AIzaSyBkKgw0HGSVc3phqiGJN7dJ0AG3diVdP40",
    )

    model = "gemini-2.5-pro"
    contents = [
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text="Hello"),
            ],
        ),
    ]
    generate_content_config = types.GenerateContentConfig(
        thinking_config = types.ThinkingConfig(
            thinking_budget=-1,
        ),
        system_instruction=[
            types.Part.from_text(text="""You're a chatbot for IIT Sri Lanka. Based on the info provided respond to the user.

Degrees
Undergraduate programmes are offered in the disciplines of IT and Business.

BSc (Hons) in Computer Science
BEng (Hons) in Software Engineering
BSc(Hons) in Artificial Intelligence and Data Science
BSc(Hons) Business Information Systems
BA (Hons) Business Management
Postgraduate Masters Programmes

MSc Advanced Software Engineering
MSc Business Analytics
MA Fashion Business Management
MSc Big Data
MSc Cyber Security and Forensics
Foundation programme.

Foundation Programme"""),
        ],
    )

    for chunk in client.models.generate_content_stream(
        model=model,
        contents=contents,
        config=generate_content_config,
    ):
        print(chunk.text, end="")

if __name__ == "__main__":
    generate()
