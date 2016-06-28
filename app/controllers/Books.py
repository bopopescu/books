from system.core.controller import *

class Books(Controller):
    def __init__(self, action):
        super(Books, self).__init__(action)
        self.load_model('Book')

    def create_book(self):
        if not request.form['new_author']:
            user_author = request.form['est_author']
        else:
            user_author = request.form['new_author']

        # book_details = request.form
        # print book_details
        # print book_details['title']
        book_details = {
            'title' : request.form['title'],
            'author' : user_author,
            'rating' : request.form['rating'],
            'user_id' : session['id']

        }
        self.models['Book'].create_book1(book_details)
        authorsid = self.models['Book'].get_author_by_id(book_details)
        books_info = {
            'author_id': authorsid['author']['id'],
            'title' : request.form['title'],
            'rating' : request.form['rating']

        }
        self.models['Book'].create_book(books_info)
        booksid = self.models['Book'].get_book_by_id(book_details)
        book_info = {
            'book_id': booksid['title']['id'],
            'rating' : request.form['rating'],
            'content' : request.form['content'],
            'user_id' : session['id']

        }
        # LEAVING OFF AT THE LINE ABOVE TO CREATE get_book_by_id IN MODEL
        self.models['Book'].create_book2(book_info)
        return redirect('/')

    def add(self):
        return self.load_view('add.html') 

    def home(self):
        return self.load_view('home.html')


