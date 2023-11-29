**CRUD operations Book Table**

Read Records:
-- Read all records from the Book table
    SELECT * FROM Book;
-- Read a specific book by ISBN
    SELECT * FROM Book WHERE ISBN = '8754471935';

Insert Statement:
-- Insert a new book into the Book table
    INSERT INTO Book (ISBN, Title, Author, Edition, PublishedYear, BookLocation)
VALUES ('8754471945', 'New Book', 'New Author', 'First Edition', 2023, 'A1.1.105');

Update Statement:  
-- Update the information for a specific book
    UPDATE Book
    SET Title = 'Updated Book', Edition = 'Second Edition'
    WHERE ISBN = '8754471945';

Delete Statement:
-- Delete a specific book by ISBN
    DELETE FROM Book WHERE ISBN = '8754471945';

**CRUD operations Author Table**

Read Records: 
-- Read all records from the Author table
    SELECT * FROM Author;

-- Read a specific author by AuthorID
    SELECT * FROM Author WHERE AuthorID = '72549';

Insert Statement:
-- Insert a new author into the Author table
    INSERT INTO Author (AuthorID, AuthorName, AuthorNationality, AuthorEmail, AuthorWebsite)
    VALUES ('72554', 'New Author', 'New Nationality', 'newauthor@example.com', 'https://www.newauthor.com');

Update Statement:
-- Update the information for a specific author
    UPDATE Author
    SET AuthorName = 'Updated Author', AuthorEmail = 'updatedauthor@example.com'
    WHERE AuthorID = '72554';

Delete Statement:
-- Delete a specific author by AuthorID
    DELETE FROM Author WHERE AuthorID = '72554';

**CRUD operations LibraryMember Table**

Read Records:
-- Read all records from the LibraryMember table
    SELECT * FROM LibraryMember;
-- Read a specific library member by MemberID
    SELECT * FROM LibraryMember WHERE MemberID = '72549';

Insert Statement:
-- Insert a new library member into the LibraryMember table
    INSERT INTO LibraryMember (MemberID, FirstName, LastName, Address, Mobile, Email)
    VALUES ('72555', 'New', 'Member', 'New Address', '9876543210', 'newmember@example.com');

Update Statement:
-- Update the information for a specific library member
    UPDATE LibraryMember
    SET FirstName = 'Updated', Mobile = '1112223333'
    WHERE MemberID = '72555';

Delete Statement:
-- Delete a specific library member by MemberID
    DELETE FROM LibraryMember WHERE MemberID = '72555';

**CRUD operations BookLoan Table**

Read Records:
-- Read all records from the BookLoan table
    SELECT * FROM BookLoan;

-- Read a specific loan by LoanID
    SELECT * FROM BookLoan WHERE LoanID = '8754471940';

Insert Statement:
-- Insert a new loan into the BookLoan table
    INSERT INTO BookLoan (LoanID, ISBN, MemberID, LoanDate, ReturnDate)
    VALUES ('8754471946', '8754471935', '72549', '2023-06-01', '2023-07-01');

Update Statement:
-- Update the information for a specific loan
    UPDATE BookLoan
    SET ReturnDate = '2023-08-01'
    WHERE LoanID = '8754471946';

Delete Statement:
-- Delete a specific loan by LoanID
    DELETE FROM BookLoan WHERE LoanID = '8754471946';