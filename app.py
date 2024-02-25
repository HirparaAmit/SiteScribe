from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get', methods=['GET','POST'])
def chat():
    if request.method == 'POST':
        msg = request.form['msg']
        return f"This is your input message: {msg}"