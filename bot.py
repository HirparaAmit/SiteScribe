import google.generativeai as genai
import os
from langchain_community.document_loaders import WebBaseLoader

url = 'https://arxiv.org/abs/2402.05935'
loader = WebBaseLoader(url)
data = loader.load()
print(data[0].page_content)

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel('gemini-pro')

while True:
    question = input("Enter your query: ")
    prompt = f"""Answer the question as precise as possible using the provided context. This context is scraped from a website, so if user mentions website, he means this given context.
                    Only return the helpful answer below and nothing else.\n\n
                    Context: \n {data[0].page_content}?\n
                    Question: \n {question} \n
                    Answer:
                """
    response = model.generate_content(prompt)
    print(response.text)