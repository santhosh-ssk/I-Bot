from flask import Flask, render_template, request,jsonify
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer
import urllib
app = Flask(__name__)

chatbot=ChatBot(
    'i-Bot',
    storage_adapter = "chatterbot.storage.MongoDatabaseAdapter",
    database = "i-bot",
    database_uri = "mongodb://Roy:"+urllib.parse.quote("Roy@123")+"@ds121309.mlab.com:21309/i-bot",
    logic_adapters=[
        "chatterbot.logic.BestMatch",
        'chatterbot.logic.MathematicalEvaluation',
    ],
    read_only=True
    )

chatbot.set_trainer(ListTrainer)

@app.route("/")
def home():
	return "welcome"

@app.route("/api/chat", methods=['POST'])
def chat():
    userText = request.json['msg']
    return jsonify(response=str(chatbot.get_response(userText)))

@app.route("/api/learn", methods=['POST'])
def learn():
    conversation = request.json['msg']
    if len(conversation) !=2:
    	return jsonify(error="invalid no of conversations")
    else:
    	chatbot.train(conversations)
    	return jsonify(response="success")

if __name__ == "__main__":
    app.run(debug=True)
