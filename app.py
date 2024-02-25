from flask import Flask, render_template, request
import google.generativeai as genai
import os
from langchain_community.document_loaders import WebBaseLoader

app = Flask(__name__)

# url = 'https://arxiv.org/abs/2402.05935'
# loader = WebBaseLoader(url)
# data = loader.load()

# genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
# model = genai.GenerativeModel('gemini-pro')

@app.route('/')
def index():
    return render_template('index.html')

# @app.route('/get', methods=['GET','POST'])
# def chat():
#     if request.method == 'POST':
#         msg = request.form['msg']
#         prompt = f"""Answer the question as precise as possible using the provided context. This context is scraped from a website, so if user mentions website, he means this given context.\n\n
#                     Context: \n {data[0].page_content}?\n
#                     Question: \n {msg} \n
#                     Answer:
#                 """
#         response = model.generate_content(prompt)
#         return response.text