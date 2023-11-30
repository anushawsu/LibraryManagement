Module 1: Book
Table Name: Book
Description:
The Book table serves as a central repository for information related to books in your library.
The ISBN field acts as a unique identifier for each book.
Information such as the title, author, edition, published year, and book location is stored for each book.
This table adheres to the 3rd Normal Form (3NF), as all non-prime attributes (Title, Author, Edition, PublishedYear, BookLocation) are fully functionally dependent on the primary key (ISBN), and there are no transitive dependencies.
Module 2: Author
Table Name: Author
Description:
The Author table manages details about authors associated with the books in your library.
The AuthorID field serves as a unique identifier for each author.
Information such as the author's name, nationality, email, and website is stored.
This table is in 3rd Normal Form, with all non-prime attributes fully dependent on the primary key (AuthorID).
Module 3: Library Member
Table Name: LibraryMember
Description:
The LibraryMember table stores information about individuals who are members of the library.
The MemberID field acts as a unique identifier for each library member.
Details such as first name, last name, address, mobile number, and email address are maintained for each member.
This table is in 3rd Normal Form, with all non-prime attributes fully dependent on the primary key (MemberID).
Module 4: Book Loan
Table Name: BookLoan
Description:
The BookLoan table captures the borrowing transactions in the library, linking books to library members.
The LoanID field provides a unique identifier for each loan transaction.
ISBN and MemberID fields serve as foreign keys, establishing relationships with the Book and LibraryMember tables, respectively.
LoanDate and ReturnDate store information about when a book was borrowed and when it is expected to be returned.
This table is in 3rd Normal Form, and foreign key relationships ensure referential integrity with the Book and LibraryMember tables.
Relationships
Book to Author Relationship:
The Author information in the Book table establishes a relationship between books and their respective authors.
Book Loan Relationships:
The BookLoan table establishes relationships between books (via ISBN) and library members (via MemberID), recording the borrowing and return transactions.
Normalization
1st Normal Form (1NF):
All tables have atomic values in each column, and each column has a unique name.
2nd Normal Form (2NF):
Each table is in 1NF, and all non-prime attributes are fully functionally dependent on the primary key.
3rd Normal Form (3NF):
Each table is in 2NF, and there are no transitive dependencies. Non-prime attributes are not dependent on other non-prime attributes.