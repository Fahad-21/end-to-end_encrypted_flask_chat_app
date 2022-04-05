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