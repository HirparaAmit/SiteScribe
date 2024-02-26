from flask import Flask, render_template, request, redirect, session
import google.generativeai as genai
import os, uuid
from langchain_community.document_loaders import WebBaseLoader

app = Flask(__name__)
app.config['SECRET_KEY'] = 'd5fb8c4fa8bd46638dadc4e751e0d68d'

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel('gemini-pro')

@app.route('/')
def index():
    if 'session_id' in session:
        return render_template('index.html', context='True')
    else:
        return render_template('index.html', context='False')

@app.route('/link', methods=['POST'])
def link():
    link = request.form['url']
    loader = WebBaseLoader(link)
    data = loader.load()
    if 'session_id' in session:
        with open(f"./scraped_data/{session.get('session_id')}.txt", 'w', encoding='utf-8') as file:
            file.write(data[0].page_content)
        return redirect("/")
    else:
        uid = str(uuid.uuid4())
        session['session_id'] = uid
        with open(f'scraped_data/{uid}.txt', 'w', encoding='utf-8') as file:
            file.write(data[0].page_content)
        return redirect("/")

@app.route('/get', methods=['POST'])
def chat():
    with open(f"./scraped_data/{session.get('session_id')}.txt", 'r', encoding='utf-8') as file:
        context = file.read()
    msg = request.form['msg']
    prompt = f"""Answer the question as precise as possible using the provided context. This context is scraped from a website, so if user mentions website, he means this given context.\n\n
                Context: \n {context}?\n
                Question: \n {msg} \n
                Answer:
            """
    response = model.generate_content(prompt)
    return response.text

if __name__=='__main__':
    app.run()