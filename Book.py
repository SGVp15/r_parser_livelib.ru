class Book:
    def __init__(self, title, author, year, isbn, rating=0, total_read=0):
        self.title = title
        self.author = author
        self.year = year
        self.isbn = isbn
        self.rating = str(rating)
        self.total_read = str(total_read)

    def __str__(self):
        return '\t'.join([self.title, self.author, self.year, self.rating, self.total_read])
