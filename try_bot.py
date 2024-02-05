import google.generativeai as genai
import os, requests
from bs4 import BeautifulSoup
from langchain_community.document_loaders import WebBaseLoader

url = 'https://www.apple.com/in/macbook-pro/'
loader = WebBaseLoader(url)
data = loader.load()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel('gemini-pro')

while True:
    question = input("Enter your query: ")
    prompt = f"""Answer the question as precise as possible using the provided context. If the answer is
                    not contained in the context, say "answer not available in context" \n\n
                    Context: \n {data[0].page_content}?\n
                    Question: \n {question} \n
                    Answer:
                """
    response = model.generate_content(prompt)
    print(response.text)