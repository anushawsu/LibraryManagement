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

# Home page
@app.route('/')
def index():
    return render_template('index.html')

# Define a route for displaying authors
@app.route('/authors_index', methods=['GET', 'POST'])
def authors_index():
    # Connect to the database
    conn = get_db()
    cursor = conn.cursor()

    if request.method == 'POST':
        # If a search form is submitted
        search_query = request.form.get('search')
        cursor.execute('''
            SELECT * FROM Author
            WHERE AuthorID LIKE ? OR AuthorName LIKE ? OR AuthorNationality LIKE ? OR AuthorEmail LIKE ? OR AuthorWebsite LIKE ?
        ''', ('%' + search_query + '%', '%' + search_query + '%', '%' + search_query + '%', '%' + search_query + '%', '%' + search_query + '%'))
        authors = cursor.fetchall()
    else:
        # Retrieve all authors from the Author table
        cursor.execute('SELECT * FROM Author')
        authors = cursor.fetchall()

    # Close the cursor and database connection
    cursor.close()
    conn.close()

    # Render the template with the list of authors
    return render_template('authors_index.html', authors=authors)

#Add Author
@app.route('/add_author', methods=['GET', 'POST'])
def add_author():
    if request.method == 'POST':
        # Get form data
        author_name = request.form.get('author_name')
        author_nationality = request.form.get('author_nationality')
        author_email = request.form.get('author_email')
        author_website = request.form.get('author_website')

        # Generate a 5-digit author ID
        author_id = generate_author_id()

        # Connect to the database
        conn = get_db()
        cursor = conn.cursor()

        # Insert a new author into the Author table
        cursor.execute('''
            INSERT INTO Author (AuthorID, AuthorName, AuthorNationality, AuthorEmail, AuthorWebsite)
            VALUES (?, ?, ?, ?, ?)
        ''', (author_id, author_name, author_nationality, author_email, author_website))

        # Commit the changes and close the cursor and database connection
        conn.commit()
        cursor.close()
        conn.close()

        # Redirect to the authors index page
        return redirect('/authors_index')
    else:
        return render_template('add_author.html')

def generate_author_id():
    # Generate a random 5-digit number as the author ID
    return str(random.randint(10000, 99999))

#Delete Author
@app.route('/delete_author/<int:author_id>', methods=['POST'])
def delete_author(author_id):
    # Connect to the database
    conn = get_db()
    cursor = conn.cursor()

    # Delete the author from the Author table based on the given author_id
    cursor.execute('DELETE FROM Author WHERE AuthorID = ?', (author_id,))

    # Commit the changes and close the cursor and database connection
    conn.commit()
    cursor.close()
    conn.close()

    # Redirect to the authors index page
    return redirect('/authors_index')



# Add_book route
@app.route('/add_book', methods=['GET', 'POST'])
def add_book():
    if request.method == 'POST':
        # Get form data
        title = request.form.get('title')
        author_id = request.form.get('author')  # Use author_id instead of author name
        edition = request.form.get('edition')
        published_year = request.form.get('published_year')
        book_location = request.form.get('book_location')

        # Generate a new ISBN
        isbn = generate_isbn()

        # Connect to the database
        conn = get_db()
        cursor = conn.cursor()

        # Insert a new book into the Book table
        cursor.execute('''
            INSERT INTO Book (ISBN, Title, Author, Edition, PublishedYear, BookLocation)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (isbn, title, author_id, edition, published_year, book_location))

        # Commit the changes and close the cursor and database connection
        conn.commit()
        cursor.close()
        conn.close()

        # Redirect to the book index page
        return redirect('/book_index')
    else:
        # Fetch authors for the dropdown
        conn = get_db()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM Author')
        authors = cursor.fetchall()
        cursor.close()
        conn.close()

        return render_template('add_book.html', authors=authors)

def generate_isbn():
    # Generate a random 10-digit number as the ISBN
    return str(random.randint(1000000000, 9999999999))









    # Run the application
if __name__ == '__main__':
    app.run(debug=True)