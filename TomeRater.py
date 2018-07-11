class User(object):
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.books = {}

    def get_email(self):
        return self.email

    def get_name(self):
        return self.name

    def change_email(self, address):
        if address is str and '@' in address:
            self.email = address
            print("User {address} address updated".format(address=address))

    def __repr__(self):
        return "User {name}, email: {email}, books read: {books}".format(name=self.name, email=self.email, books=len(self.books))

    def __eq__(self, other_user):
        try:
            if self.name == other_user.get_name() and self.email == other_user.get_email():
                return True
            else:
                return False
        except AttributeError:
            return False

    def read_book(self, book, rating=None):
        self.books[book]=rating

    def get_average_rating(self):
        count = 0
        total = 0
        for book, rating in self.books.items():
            if rating != None:
                count += 1
                total += rating
        if count > 0:
            return total / count
        else:
            return None

class Book:
    def __init__(self, title, isbn):
        self.title = title
        self.isbn = isbn
        self.ratings = []

    def __repr__(self):
        return "{title} with ISBN {isbn}".format(title=self.title, isbn=self.isbn)

    def get_title(self):
        return self.title

    def get_isbn(self):
        return self.isbn

    def set_isbn(self, new_isbn):
        if new_isbn is int or new_isbn is float:
            old_isbn = self.isbn
            self.isbn = new_isbn
            print("{title} ISBN changed from {old_isbn} to {new_isbn}.".format(title=self.title, old_isbn=old_isbn, new_isbn=self.isbn))

    def add_rating(self, rating):
        if rating >=0 and rating <=4:
                self.ratings.append(rating)
        else:
            print('Invalid rating')

    def __eq__(self, other_book):
        if self.title == other_book.get_title() and self.isbn == other_user.get_isbn():
            return True
        else:
            return False

    def get_average_rating(self):
        count = 0
        total = 0
        for rating in self.ratings:
            if rating != None:
                count += 1
                total += rating
        if count > 0:
            return total / count
        else:
            return None

    def __hash__(self):
        return hash((self.title, self.isbn))

class Fiction(Book):
    def __init__(self, title, author, isbn):
        super().__init__(title, isbn)
        self.author = author
        
    def get_author(self):
        return self.author

    def __repr__(self):
        return "{title} by {author}".format(title=self.title, author=self.author)

class Non_Fiction(Book):
    def __init__(self, title, subject, level, isbn):
        super().__init__(title, subject)
        self.subject = subject
        self.level = level
        
    def get_subject(self):
        return self.subject

    def get_level(self):
        return self.level

    def __repr__(self):
        return "{title}, a {level} manual on {subject}".format(title=self.title, level=self.level, subject=self.subject)

class TomeRater:
    def __init__(self):
        self.users = {}
        self.books = {}
    
    def create_book(self, title, isbn):
        return Book(title, isbn)

    def create_novel(self, title, author, isbn):
        return Fiction(title, author, isbn)

    def create_non_fiction(self, title, subject, level, isbn):
        return Non_Fiction(title, subject, level, isbn)

    def add_book_to_user(self, book, email, rating=None):
        if email in self.users.keys():
            user = self.users[email]
            user.read_book(book, rating)
            if rating != None:
                book.add_rating(rating)
            if book not in self.books:
                self.books[book]=1
            else:
                self.books[book]+=1
        else:
            print("No user with email {email}!".format(email=email))
     
    def add_user(self, name, email, user_books=None):
        if email not in self.users.keys():
            self.users[email]=User(name, email)
            if user_books != None:
                for book in user_books:
                    self.add_book_to_user(book, email) 

    def print_catalog(self):
        for book in self.books.keys():
            print(book)

    def print_users(self):
        for user in self.users.values():
            print(user)

    def get_most_read_book(self):
        max_reads = 0
        max_book = None
        for book, reads in self.books.items():
            if reads > max_reads:
                max_reads = reads
                max_book = book
        return max_book

    def highest_rated_book(self):
        max_rating = 0
        max_book = None
        for book in self.books.keys():
            rating = book.get_average_rating()
            if rating > max_rating:
                max_rating = rating
                max_book = book
        return max_book
    
    def most_positive_user(self):
        max_ave_rating = 0
        max_user = None
        for user in self.users.values():
            rating = user.get_average_rating()
            if rating != None:
                if rating > max_ave_rating:
                    max_ave_rating = rating
                    max_user = user
        return max_user
        

        
