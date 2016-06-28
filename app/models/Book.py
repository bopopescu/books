from system.core.model import *

class Book(Model):
    def __init__(self):
        super(Book, self).__init__()


    def create_book(self, info):

        query = "INSERT INTO books (title, rating, created_at, updated_at, author_id) VALUES (%s, %s, NOW(), NOW(), %s)"
        data = [info['title'], info['rating'], info['author_id']] 
        return self.db.query_db(query, data)

    def create_book1(self, info):
        query2 = "INSERT INTO authors (name, created_at, updated_at) VALUES (%s, NOW(), NOW())"
        data2 = [info['author']]
        return self.db.query_db(query2, data2)


    def create_book2(self, info):
        query3 = "INSERT INTO reviews (content, user_id, book_id, created_at, updated_at) VALUES (%s, %s, %s, NOW(), NOW())"
        data3 = [info['content'], info['user_id'], info['book_id']]
        return self.db.query_db(query3, data3)

    def get_author_by_id(self,info):
        query = "SELECT * FROM authors WHERE authors.name = %s ORDER BY created_at DESC"
        values = [info['author']]
        author= self.db.query_db(query, values)
        return {'author': author[0]}


    def get_book_by_id(self, id):
    	query = "SELECT id FROM books WHERE books.title = %s ORDER BY created_at DESC LIMIT 1"
    	data = [id['title']]
    	libro = self.db.query_db(query, data)
        return {'title': libro[0]}