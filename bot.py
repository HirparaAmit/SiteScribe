import google.generativeai as genai
import os
from langchain_community.document_loaders import WebBaseLoader

url = 'https://www.amazon.com/A315-24P-R7VH-Display-Quad-Core-Processor-Graphics/dp/B0BS4BP8FB/ref=sr_1_9?keywords=laptop&sr=8-9'
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