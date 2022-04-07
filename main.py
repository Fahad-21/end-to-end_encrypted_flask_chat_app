from flask import Flask, render_template, request, redirect, url_for
from flask_mail import Mail,Message
from random import randint
from flask_socketio import SocketIO, emit, send
import pyAesCrypt
import io as k

key = ''
bufferSize = 64 * 1024
password = "please-use-a-long-and-random-password"
app = Flask(__name__, template_folder='templates')
mail = Mail(app)
my_addr = 'verifytext7@gmail.com'
app.config["MAIL_SERVER"] = 'smtp.gmail.com'
app.config["MAIL_PORT"] = 465
app.config["MAIL_USERNAME"] = my_addr
app.config['MAIL_PASSWORD'] = 'Pak=12345'                   #you have to give your password of gmail account
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)
otp = randint(000000,999999)

app = Flask(__name__)
io = SocketIO(app)

messages = []

@app.route("/chat")
def home():
    return render_template("chat.html")