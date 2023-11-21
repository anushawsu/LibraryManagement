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

with app.app_context():
    conn = get_db()
    cursor = conn.cursor()
    # Create the Book Table
    cursor.execute('''CREATE TABLE IF NOT EXISTS Book (
                        ISBN INTEGER PRIMARY KEY AUTOINCREMENT,
                        Title TEXT,
                        Author TEXT,
                        Edition TEXT,
                        PublishedYear INTEGER,
                        BookLocation TEXT
                    )''')

    # Create the Author Table
    cursor.execute('''CREATE TABLE IF NOT EXISTS Author (
                    AuthorID INTEGER PRIMARY KEY AUTOINCREMENT,
                    AuthorName TEXT,
                    AuthorNationality TEXT,
                    AuthorEmail TEXT,
                    AuthorWebsite TEXT
                )''')

    # Create the Library Member Table
    cursor.execute('''CREATE TABLE IF NOT EXISTS LibraryMember (
                        MemberID INTEGER PRIMARY KEY AUTOINCREMENT,
                        FirstName TEXT,
                        LastName TEXT,
                        Address TEXT,
                        Mobile TEXT,
                        Email TEXT
                    )''')

    # Create the Book Loan Table
    cursor.execute('''CREATE TABLE IF NOT EXISTS BookLoan (
                        LoanID INTEGER PRIMARY KEY AUTOINCREMENT,
                        ISBN INTEGER,
                        MemberID INTEGER,
                        LoanDate TEXT,
                        ReturnDate TEXT,
                        FOREIGN KEY (ISBN) REFERENCES Book(ISBN),
                        FOREIGN KEY (MemberID) REFERENCES LibraryMember(MemberID)
                    )''')

    conn.commit()
    cursor.close()
    conn.close()

    # Run the application
if __name__ == '__main__':
    app.run(debug=True)