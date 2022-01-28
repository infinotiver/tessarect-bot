from flask import Flask
from threading import Thread


app = Flask('WEB')

@app.route('/')
def home():
    return "I am Discord Bot and I'm vibing to Inception"
def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()