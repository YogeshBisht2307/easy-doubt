from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from videoTotext import *

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Esh@localhost/EasyDoubt'

english_bot = ChatBot('Chatterbot', storage_adapter='chatterbot.storage.SQLStorageAdapter',
                      database_uri='postgresql://postgres:Esh@localhost/EasyDoubt')

db = SQLAlchemy(app)
trainer = ChatterBotCorpusTrainer(english_bot)

trainer.train(
    './Knowledge/c.yml',
    './Knowledge/os.yml',
    './Knowledge/english.yml',
    './Knowledge/sort.yml'
)

# config for video content


class Thumbnail(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    href = db.Column(db.String(80),unique=True, nullable=False)
    image = db.Column(db.String(80), unique=True, nullable=False)
    head = db.Column(db.String(50), unique=True, nullable=False)
    desc = db.Column(db.String(200), unique=True, nullable=False)

    def __init__(self, head, image, desc):
        self.head = head
        self.image = image
        self.desc = desc


class Video_detail(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    head = db.Column(db.String(50), unique=True, nullable=False)
    desc = db.Column(db.String(200), unique=True, nullable=False)

    def __init__(self, head, desc):
        self.head = head
        self.desc = desc


class Sugg(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ques = db.Column(db.String(80), unique=True, nullable=False)

    def __init__(self, ques):
        self.ques = ques


# our home screen with all the pages for our videos

@app.route('/')
def home():

    thumb = Thumbnail.query.all()
    return render_template('home.html', thumb=thumb)

# for video 1


@app.route('/clanguage')
def cvid():
    detail = Video_detail.query.first()
    text = vidTotext1('static/clanguage.mp4')
    sugg = extract1(text)
    return render_template('video1.html', suggestion=sugg, details=detail)


# for video 2


@app.route('/osvideo')
def osvid():
    detail = Video_detail.query.filter_by(id='2').first()
    text = vidTotext4('static/osvid.mp4')
    sugg = extract4(text)
    return render_template('video2.html', suggestion=sugg, details=detail)

# for video


@app.route('/datastructure')
def dsvid():
    detail = Video_detail.query.filter_by(id='4').first()
    text = vidTotext0('static/sorting.mp4')
    sugg = extract0(text)
    return render_template('video3.html', suggestion=sugg, details=detail)


@app.route('/english')
def engvid():
    detail = Video_detail.query.filter_by(id='3').first()
    text = vidTotext2('static/engvid.mp4')
    sugg = extract2(text)
    return render_template('video4.html', suggestion=sugg, details=detail)


# for chatbot response


@app.route('/get')          # bot training module
def get_bot_response():
    userText = request.args.get('msg')
    return str(english_bot.get_response(userText))


if __name__ == '__main__':
    app.run(debug=True)
