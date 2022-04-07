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

@app.route('/', methods=['GET', 'POST'])
def form():
    global key
    if request.method == 'POST':
        user_email = request.form['text']
        print('gggg', user_email)
        key += request.form['password']
        print('key', key)
        msg = Message(subject='OTP', sender=my_addr, recipients=[user_email])
        msg.body = str(otp)
        mail.send(msg)
        return redirect(url_for('verification', usr=user_email))
    else:
        return render_template('index.html')

    @io.on('sendMessage')
    def send_message_handler(msg):
        global password, key
        print('message', msg)
        print('l', key)
        if password == str(key):
            print('f2')
            print(msg['message'])
            # binary data to be encrypted
            c = bytes(str(msg['message']), encoding='utf-8')
            print(c)
            pbdata = c