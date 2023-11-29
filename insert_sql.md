-- Insert sample data into the Book table
INSERT INTO Book (ISBN, Title, Author, Edition, PublishedYear, BookLocation) VALUES
('8754471935', 'Book1', 'Author1', 'First Edition', 2020, 'A1.1.101'),
('8754471936', 'Book2', 'Author2', 'Second Edition', 2018, 'B2.2.202'),
('8754471937', 'Book3', 'Author3', 'Third Edition', 2015, 'C3.3.303'),
('8754471938', 'Book4', 'Author1', 'Fourth Edition', 2019, 'D4.4.404'),
('8754471939', 'Book5', 'Author4', 'Fifth Edition', 2021, 'E5.5.505');

-- Insert sample data into the LibraryMember table
INSERT INTO LibraryMember (MemberID, FirstName, LastName, Address, Mobile, Email) VALUES
('72549', 'Member1', 'Last1', 'Address1', '1234567890', 'member1@example.com'),
('72550', 'Member2', 'Last2', 'Address2', '9876543210', 'member2@example.com'),
('72551', 'Member3', 'Last3', 'Address3', '1112223333', 'member3@example.com'),
('72552', 'Member4', 'Last4', 'Address4', '4445556666', 'member4@example.com'),
('72553', 'Member5', 'Last5', 'Address5', '7778889999', 'member5@example.com');

-- Insert sample data into the Author table
INSERT INTO Author (AuthorID, AuthorName, AuthorNationality, AuthorEmail, AuthorWebsite) VALUES
('72549', 'Author1', 'Nationality1', 'author1@example.com', 'https://www.author1.com'),
('72550', 'Author2', 'Nationality2', 'author2@example.com', 'https://www.author2.com'),
('72551', 'Author3', 'Nationality3', 'author3@example.com', 'https://www.author3.com'),
('72552', 'Author4', 'Nationality4', 'author4@example.com', 'https://www.author4.com'),
('72553', 'Author5', 'Nationality5', 'author5@example.com', 'https://www.author5.com');

-- Insert sample data into the BookLoan table
INSERT INTO BookLoan (LoanID, ISBN, MemberID, LoanDate, ReturnDate) VALUES
('8754471940', '8754471935', '72549', '2023-01-01', '2023-02-01'),
('8754471941', '8754471936', '72550', '2023-02-01', '2023-03-01'),
('8754471942', '8754471937', '72551', '2023-03-01', '2023-04-01'),
('8754471943', '8754471938', '72552', '2023-04-01', '2023-05-01'),
('8754471944', '8754471939', '72553', '2023-05-01', '2023-06-01');
