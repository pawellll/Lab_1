"""
@author: Paweł Pęksa
"""

import xml.etree.ElementTree as et
import sys
from pprint import pprint


class BooksParser(object):
    def __init__(self, file_path):
        try:
            self._parsedBooks = et.parse(file_path).getroot()
        except IOError as e:
            print("Failed: {0}".format(e))
            sys.exit(1)

    def parse(self):

        books_list = []

        for book in self._parsedBooks.findall('book'):
            book_id = book.get('id')
            author = book.find('author').text
            title = book.find('title').text
            genre = book.find('genre').text
            price = book.find('price').text
            publish_date = book.find('publish_date').text
            description = book.find('description').text

            book_tuple = [book_id, author, title, genre, price, publish_date, description]
            books_list.append(book_tuple)

        pprint(books_list)