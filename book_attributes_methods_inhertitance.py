# Create a class to represent a book with attributes and methods
# Implement inheritance by creating the subclass for different types of books

class Books:
    def _init_(self,title,author,page_no):
        self.title=title
        self.author=author
        self.page_no=page_no
    
class Fiction(Books):
    def _init_(self,title,author,page_no):
        super()._init_(title,author,page_no)
    
class Non_Fiction(Books):
    def _init_(self,title,author,page_no):
        super()._init_(title,author,page_no)

class Comic(Books):
    def _init_(self,title,author,page_no):
        super()._init_(title,author,page_no)

class Horror(Books):
    def _init_(self,title,author,page_no):
        super()._init_(title,author,page_no)
