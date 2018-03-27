
class User():
    """ Contains user data """

    users=[] #list for all users

    def __init__(self):
        self.public_id=None
        self.name=None
        self.password=None
        self.admin=False

#------------------------------------------------------------

class Books():
    books=[]
    """Contains books info """
    def __init__(self):
        self.book_id=None
        self.book_title=None
        self.author=None
        self.edition=None
        self.publisher=None

    def get_book_by_id(bookid):
        """Searches for one book in the list"""
        for book in Books.books:
            if book.book_id is bookid:
                return book
        return "Books is not listed"