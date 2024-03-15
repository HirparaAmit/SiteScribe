from flask import Flask, render_template, request, redirect, session, jsonify
import google.generativeai as genai
import os, uuid
from datetime import datetime
from langchain_community.document_loaders import WebBaseLoader
from apscheduler.schedulers.background import BackgroundScheduler

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv("APP_SECRET_KEY")

scheduler = BackgroundScheduler()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel('gemini-pro')

def delete_files():
    current_time = datetime.now().timestamp()
    expiration_threshold = 18000
    for file in os.listdir('./scraped_data'):
        creation_time = os.path.getctime(f"./scraped_data/{file}")
        current_time = datetime.now().timestamp()
        if current_time - creation_time > expiration_threshold:
            os.remove(f"./scraped_data/{file}")

scheduler.add_job(delete_files, 'interval', minutes=120)
scheduler.start()

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
    if 'session_id' in session:
        if f"{session.get('session_id')}.txt" in os.listdir('./scraped_data'):
            with open(f"./scraped_data/{session.get('session_id')}.txt", 'r', encoding='utf-8') as file:
                context = file.read()
            msg = request.form['msg']
            prompt = f"""Answer the question as precise as possible.\n\n
                        Context: \n {context}?\n
                        Question: \n {msg} \n
                        Answer:
                    """
            chat = model.start_chat(history=[])
            response = chat.send_message(prompt)
            return jsonify({"response": response.text, "type": "success"})
        else:
            print("Your session is timed out!")
            session.clear()
            return jsonify({"response": "Your session is timed out!", "type": "redirect"})
    else:
        return jsonify({"response": "Your session is timed out!", "type": "redirect"})

if __name__=='__main__':
    app.run()