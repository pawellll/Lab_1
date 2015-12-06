#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@author: Paweł Pęksa
"""

from BooksParser import BooksParser

if __name__ == '__main__':
    print('Lab 01 | Problem 2')
    parser = BooksParser("Books.xml")
    parser.parse()



