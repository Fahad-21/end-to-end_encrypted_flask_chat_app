from flask import Flask, render_template, request, redirect, url_for
from flask_mail import Mail,Message
from random import randint
from flask_socketio import SocketIO, emit, send
import pyAesCrypt
import io as k

key = ''
bufferSize = 64 * 1024
password = "Fahad" # u can give any password here to encrypt the messages
app = Flask(__name__, template_folder='templates')
mail = Mail(app)
my_addr = 'verifytext7@gmail.com' # mail
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
        key = request.form['password']
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
    print('l',key)
    if password == str(key):
        print('f2')
        print(msg['message'])
        # binary data to be encrypted
        c = bytes(str(msg['message']), encoding='utf-8')
        print(c)
        pbdata = c

        # input plaintext binary stream
        fIn = k.BytesIO(pbdata)

        # initialize ciphertext binary stream
        fCiph = k.BytesIO()

        # initialize decrypted binary stream
        fDec = k.BytesIO()

        # encrypt stream
        pyAesCrypt.encryptStream(fIn, fCiph, password, bufferSize)

        # print encrypted data
        print("This is the ciphertext:\n" + str(fCiph.getvalue()))
        messages.append(str(fCiph.getvalue()))
        print('messages', messages)

        print('kkkkkkkkkkkkkkkkkkkk')
        # get ciphertext length
        ctlen = len(fCiph.getvalue())

        # go back to the start of the ciphertext stream
        fCiph.seek(0)

        # decrypt stream
        pyAesCrypt.decryptStream(fCiph, fDec, password, bufferSize, ctlen)

        # print decrypted data
        print("Decrypted data:\n" + str(fDec.getvalue()))
        t = str(fDec.getvalue())
        l = t.replace('b', '')
        m = l.replace("'", '')
        n = m.replace("'", '')
        print('n', n)

        info = {
            'name' : f'{msg["name"]}' , 'message' : f'{n}'
        }
        emit('getMessage', info, broadcast=True)
    else:
        print('qqqqqqqq', messages)
        enc_info = {'name' : f'{msg["name"]}', 'messsage' : f'{messages}'}
        emit('getMessage', enc_info, broadcast=True)

@io.on('message')
def message_handler(msg):
    print('f1')
    print(msg)
    send(messages)

@app.route('/<usr>', methods=['GET', 'POST'])
def verification(usr):
    if request.method == 'POST':
        otp_data = request.form['otp_text']
        if otp == int(otp_data):
            print('otp', otp, 'otp entered', otp_data)
            print('Succesful')
            return redirect(url_for('home'))
        else:
            return '<h1>Invalid Otp</h1>'
    else:
        return render_template('otp_verification.html')

if __name__ == "__main__":
    io.run(app, debug=True)