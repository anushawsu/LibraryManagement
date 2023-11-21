# main.py
from datetime import datetime
import secrets
import string
from flask import Flask, render_template, request, redirect, g, session
import sqlite3
import uuid
from flask import render_template
import random

def generate_secret_key(length=24):
    alphabet = string.ascii_letters + string.digits + string.punctuation
    secret_key = ''.join(secrets.choice(alphabet) for _ in range(length))
    return secret_key

app = Flask(__name__)
app.secret_key = generate_secret_key()

# Database connection helper function
def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect('CS665_Group5_Library.db')
    return db



    # Run the application
if __name__ == '__main__':
    app.run(debug=True)