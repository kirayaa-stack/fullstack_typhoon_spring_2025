class Book:
    def __init__(self, title, author, pages, published_year):
        self.title = title
        self.author = author
        self.pages = pages
        self.published_year = published_year
    def age(self):
        today_year = 2025
        return today_year - self.published_year
    def page(self):
        if self.page > 300:
            print(f"Long look: Yes")
        else:
            print(f"Long book: No")
            
book1 = Book("The Hobbit", "J.R.R. Tolkien", 295, 1937)
book2 = Book("War and Peace", "Leo Tolstoy", 1225, 1869)
book3 = Book("Python Crash Course", "Eric Matthes", 544, 2019)
books = [book1, book2, book3]
     
print(Book)
    

