from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer

app = Flask(__name__)

chatbot=ChatBot(
    'Bot',
    database='./database/database.sqlite3',
    storage_adapter="chatterbot.storage.SQLStorageAdapter",
    logic_adapters=[
        "chatterbot.logic.BestMatch",
        'chatterbot.logic.MathematicalEvaluation',
    ],
    read_only=True
    )

chatbot.set_trainer(ListTrainer)
conversation=[
    "let us start learning",
    "let us start learning"]

chatbot.train(conversation)
conversation=[
    "that it",
    "that it"
]

chatbot.train(conversation)
conversation=[
    "stop",
    "stop"
]
chatbot.train(conversation)

chatbot.train(conversation)
conversation=[
    "how are you?",
    "iam fine."
]
chatbot.train(conversation)

@app.route("/")
def home():chatbot.get_response("how are you")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return str(chatbot.get_response(userText))


if __name__ == "__main__":
    app.run(debug=True)
