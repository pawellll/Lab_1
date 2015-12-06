#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@author: Paweł Pęksa
"""

import xml.etree.ElementTree as et
import sys
import logging
from pprint import pprint


class BooksParser(object):
    def __init__(self, file_path):
        self._books_list = []
        try:
            self._parsedBooks = et.parse(file_path).getroot()
        except Exception as e:
            logging.error(e)
            sys.exit(1)

    def parse(self):
        for book in self._parsedBooks.findall('book'):
            book_tuple = self.parse_book(book)
            self._books_list.append(book_tuple)

    def print_books(self):
        pprint(self._books_list)

    @staticmethod
    def parse_book(book):
        book_id = book.get('id')
        author = book.find('author').text
        title = book.find('title').text
        genre = book.find('genre').text
        price = book.find('price').text
        publish_date = book.find('publish_date').text
        description = book.find('description').text

        return [book_id, author, title, genre, price, publish_date, description]