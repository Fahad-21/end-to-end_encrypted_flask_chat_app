from flask import Flask, render_template, request, redirect, url_for
from flask_mail import Mail,Message
from random import randint
from flask_socketio import SocketIO, emit, send