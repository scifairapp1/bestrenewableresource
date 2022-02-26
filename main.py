import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
import pandas as pd
import flask

import os
os.environ['DISPLAY'] = ':0'
from sklearn import linear_model

app = flask.Flask(__name__)

@app.route('/')

@app.route('/home')
def home():
    return "Hello World"





if __name__ == '__main__':
    app.run()
