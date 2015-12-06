#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@author: Paweł Pęksa
"""

import unittest
from src.BooksParser import BooksParser
import xml.etree.ElementTree as ET


class BookParserTest(unittest.TestCase):
    def test_init_1(self):
        with self.assertRaises(SystemExit):
            book_parser = BooksParser("no_exist")

    def test_init_2(self):
        with self.assertRaises(SystemExit):
            book_parser = BooksParser("")

    def test_parse_1(self):
        parser = BooksParser("Books.xml")
        parser.parse()
        self.assertNotEqual(0, len(parser._books_list))

    def testIfXMLIncorrect(self):
        parser = BooksParser("invalidBooks.xml")
        self.assertRaises(ET.ParseError)

if __name__ == '__main__':
    unittest.main()
