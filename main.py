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

# Update Author
@app.route('/update_author/<int:author_id>', methods=['GET', 'POST'])
def update_author(author_id):
    # Connect to the database
    conn = get_db()
    cursor = conn.cursor()

    if request.method == 'POST':
        # Get form data
        author_name = request.form.get('author_name')
        author_nationality = request.form.get('author_nationality')
        author_email = request.form.get('author_email')
        author_website = request.form.get('author_website')

        # Update the author in the Author table based on the given author_id
        cursor.execute('''
            UPDATE Author
            SET AuthorName = ?, AuthorNationality = ?, AuthorEmail = ?, AuthorWebsite = ?
            WHERE AuthorID = ?
        ''', (author_name, author_nationality, author_email, author_website, author_id))

        # Commit the changes and close the cursor and database connection
        conn.commit()
        cursor.close()
        conn.close()

        # Redirect to the authors index page after updating
        return redirect('/authors_index')
    else:
        # Retrieve existing author details for the specified author_id
        cursor.execute('SELECT * FROM Author WHERE AuthorID = ?', (author_id,))
        author_details = cursor.fetchone()

        # Close the cursor and database connection
        cursor.close()
        conn.close()

        if author_details:
            # Render the update_author.html template with the existing author details
            return render_template('update_author.html', author=author_details)
        else:
            # Handle case where author_id is not found
            return "Author not found."



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

# Define a route for displaying all library members
@app.route('/library_members_index', methods=['GET', 'POST'])
def library_members_index():
    # Connect to the database
    conn = get_db()
    cursor = conn.cursor()

    if request.method == 'POST':
        # If a search form is submitted
        search_query = request.form.get('search')
        cursor.execute('''
            SELECT * FROM LibraryMember
            WHERE MemberID LIKE ? OR FirstName LIKE ? OR LastName LIKE ? OR Address LIKE ? OR Mobile LIKE ? OR Email LIKE ?
        ''', ('%' + search_query + '%', '%' + search_query + '%', '%' + search_query + '%', '%' + search_query + '%', '%' + search_query + '%', '%' + search_query + '%'))
        members = cursor.fetchall()
    else:
        # Retrieve all library members from the LibraryMember table
        cursor.execute('SELECT * FROM LibraryMember')
        members = cursor.fetchall()

    # Close the cursor and database connection
    cursor.close()
    conn.close()

    # Render the template with the list of library members
    return render_template('library_members_index.html', members=members)


# Route for displaying all books
@app.route('/book_index', methods=['GET', 'POST'])
def book_index():
    # Connect to the database
    conn = get_db()
    cursor = conn.cursor()

    if request.method == 'POST':
        # If a search form is submitted
        search_query = request.form.get('search')
        cursor.execute('''
            SELECT Book.ISBN, Book.Title, Author.AuthorName, Book.Edition, Book.PublishedYear, Book.BookLocation
            FROM Book
            INNER JOIN Author ON Book.Author = Author.AuthorID
            WHERE Book.Title LIKE ? OR Author.AuthorName LIKE ? OR Book.BookLocation LIKE ?
        ''', ('%' + search_query + '%', '%' + search_query + '%', '%' + search_query + '%'))
        books = cursor.fetchall()
    else:
        # Retrieve all books from the Book table with author names
        cursor.execute('''
            SELECT Book.ISBN, Book.Title, Author.AuthorName, Book.Edition, Book.PublishedYear, Book.BookLocation
            FROM Book
            INNER JOIN Author ON Book.Author = Author.AuthorID
        ''')
        books = cursor.fetchall()

    # Close the cursor and database connection
    cursor.close()
    conn.close()

    # Render the template with the list of books
    return render_template('book_index.html', books=books)

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

# Update the route for rendering the update book page
@app.route('/book_update/<int:isbn>', methods=['GET', 'POST'])
def book_update(isbn):
    # Connect to the database
    conn = get_db()
    cursor = conn.cursor()

    if request.method == 'POST':
        # Get form data
        title = request.form.get('title')
        author = request.form.get('author')
        edition = request.form.get('edition')
        published_year = request.form.get('published_year')
        book_location = request.form.get('book_location')

        # Update the book in the Book table based on the given ISBN
        cursor.execute('''
            UPDATE Book
            SET Title = ?, Author = ?, Edition = ?, PublishedYear = ?, BookLocation = ?
            WHERE ISBN = ?
        ''', (title, author, edition, published_year, book_location, isbn))

        # Commit the changes and close the cursor and database connection
        conn.commit()
        cursor.close()
        conn.close()

        # Redirect to the book index page after updating
        return redirect('/book_index')
    else:
        # Retrieve existing book details for the specified ISBN
        cursor.execute('SELECT * FROM Book WHERE ISBN = ?', (isbn,))
        book_details = cursor.fetchone()
        cursor.execute('SELECT AuthorName FROM Author WHERE AuthorID = ?', (book_details[2],))
        authorname = cursor.fetchone()[0]

        # Close the cursor and database connection
        cursor.close()
        conn.close()

        if book_details:
            # Render the update_book.html template with the existing book details
            return render_template('update_book.html', book=book_details, aname=authorname)
        else:
            # Handle case where ISBN is not found
            return "Book not found."
        
        # Define a route for deleting a book
@app.route('/book_delete/<int:isbn>', methods=['POST'])
def delete_book(isbn):
    # Connect to the database
    conn = get_db()
    cursor = conn.cursor()

    # Delete the book from the Book table based on the given ISBN
    cursor.execute('DELETE FROM Book WHERE ISBN = ?', (isbn,))

    # Commit the changes and close the cursor and database connection
    conn.commit()
    cursor.close()
    conn.close()

    # Redirect to the book index page
    return redirect('/book_index')









    # Run the application
if __name__ == '__main__':
    app.run(debug=True)