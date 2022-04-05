from flask import Flask, render_template, request, redirect, url_for
from flask_mail import Mail,Message
from random import randint
from flask_socketio import SocketIO, emit, send
import pyAesCrypt
import io as k

key = ''
bufferSize = 64 * 1024
password = "please-use-a-long-and-random-password"