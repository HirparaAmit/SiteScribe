from flask import Flask, render_template, request, session, redirect
import google.generativeai as genai
import os
from langchain_community.document_loaders import WebBaseLoader

app = Flask(__name__)
app.secret_key = 'd5fb8c4fa8bd46638dadc4e751e0d68d'

context = {'data':""}
# url = 'https://arxiv.org/abs/2402.05935'

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel('gemini-pro')

@app.route('/')
def index():
    global context
    return render_template('index.html', context=context)

@app.route('/link', methods=['POST'])
def link():
    link = request.form['url']
    loader = WebBaseLoader(link)
    data = loader.load()
    global context
    context = {'data':data[0].page_content}
    return redirect("/")

@app.route('/get', methods=['GET','POST'])
def chat():
    if request.method == 'POST':
        global context
        msg = request.form['msg']
        prompt = f"""Answer the question as precise as possible using the provided context. This context is scraped from a website, so if user mentions website, he means this given context.\n\n
                    Context: \n {context['data']}?\n
                    Question: \n {msg} \n
                    Answer:
                """
        response = model.generate_content(prompt)
        return response.text