import google.generativeai as genai
import os

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel('gemini-pro')

text_file_path = './output.txt'
with open(text_file_path, 'r', encoding='utf-8') as file:
    context = file.read()

while True:
    question = input("Enter your query: ")
    prompt = f"""Answer the question as precise as possible using the provided context. If the answer is
                    not contained in the context, say "answer not available in context" \n\n
                    Context: \n {context}?\n
                    Question: \n {question} \n
                    Answer:
                """
    response = model.generate_content(prompt)
    print(response.text)