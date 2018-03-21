from flask import Flask, render_template, request,jsonify
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer
import urllib
import json,requests
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
    #print(request.json['msg'])
    conversation = request.json['msg']
    if len(conversation) !=2:
    	return jsonify(error="invalid no of conversations")
    else:
    	chatbot.train(conversation)
    	return jsonify(response="success")

headers = {
    "Content-Type": "application/json",
}

@app.route("/api/translate", methods=['POST'])
def translate():
    #print(request.json['msg'])
	requestPayload = {
	    "to": email_data['to'],
	    "from": "admin@project.com",
	    "fromName": "SVCE Grievance Redressal Committee",
	    "sub": email_data["sub"],
	    "text": email_data["text"],
	    "html": email_data["html"]
	}
	resp = requests.request("POST","https://translate.yandex.net/api/v1.5/tr.json/translate ?key=trnsl.1.1.20180321T182122Z.0744c55b609c1cca.0377b6bfa4fd2ff3b9efb061d71df78173b6a017& text="+request.json["text"]+"& lang="+request.json["from"]+"-"+request.json["to"], headers=headers)
	return jsonify(json.loads(resp.content))

if __name__ == "__main__":
    app.run(debug=True)
