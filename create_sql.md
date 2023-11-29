**-- Create the Book Table**
CREATE TABLE IF NOT EXISTS Book (
    ISBN INTEGER PRIMARY KEY AUTOINCREMENT,
    Title TEXT,
    Author TEXT,
    Edition TEXT,
    PublishedYear INTEGER,
    BookLocation TEXT
);

**-- Create the Author Table**
CREATE TABLE IF NOT EXISTS Author (
    AuthorID INTEGER PRIMARY KEY AUTOINCREMENT,
    AuthorName TEXT,
    AuthorNationality TEXT,
    AuthorEmail TEXT,
    AuthorWebsite TEXT
);

**-- Create the Library Member Table**
CREATE TABLE IF NOT EXISTS LibraryMember (
    MemberID INTEGER PRIMARY KEY AUTOINCREMENT,
    FirstName TEXT,
    LastName TEXT,
    Address TEXT,
    Mobile TEXT,
    Email TEXT
);

**-- Create the Book Loan Table**
CREATE TABLE IF NOT EXISTS BookLoan (
    LoanID INTEGER PRIMARY KEY AUTOINCREMENT,
    ISBN INTEGER,
    MemberID INTEGER,
    LoanDate TEXT,
    ReturnDate TEXT,
    FOREIGN KEY (ISBN) REFERENCES Book(ISBN),
    FOREIGN KEY (MemberID) REFERENCES LibraryMember(MemberID)
);


To check whether the tables are in 3rd Normal Form (3NF) or not, we need to ensure that they satisfy the following conditions:

**First Normal Form (1NF):** All columns must contain atomic (indivisible) values, and each column must have a unique name.

**Second Normal Form (2NF):** It should be in 1NF, and all non-prime attributes (attributes not part of the primary key) should be fully functionally dependent on the primary key.

**Third Normal Form (3NF):** It should be in 2NF, and no transitive dependencies should exist. In other words, if a non-prime attribute is transitively dependent on the primary key, it should be moved to a separate table.

Let's analyze each table:

**Book Table:**
ISBN (Primary Key): Atomic, unique.
Title, Author, Edition, PublishedYear, BookLocation: All attributes are dependent on the primary key (ISBN), and there are no transitive dependencies.
The Book table is in 3NF.

**Author Table:**
AuthorID (Primary Key): Atomic, unique.
AuthorName, AuthorNationality, AuthorEmail, AuthorWebsite: All attributes are dependent on the primary key (AuthorID).
The Author table is in 3NF.

**Library Member Table:**
MemberID (Primary Key): Atomic, unique.
FirstName, LastName, Address, Mobile, Email: All attributes are dependent on the primary key (MemberID).
The Library Member table is in 3NF.

**BookLoan Table:**
LoanID (Primary Key): Atomic, unique.
ISBN, MemberID, LoanDate, ReturnDate: All attributes are dependent on the primary key (LoanID).
There are foreign key relationships with Book(ISBN) and LibraryMember(MemberID).
The BookLoan table is in 3NF.

In summary, all the tables (Book, Author, LibraryMember, and BookLoan) appear to be in 3rd Normal Form.