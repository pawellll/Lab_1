#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@author: Paweł Pęksa
"""

from src.BooksParser import BooksParser
import logging

if __name__ == '__main__':
    logging.info('Lab 01 | Problem 2')
    parser = BooksParser("Books.xml")
    parser.parse()
    parser.print_books()



