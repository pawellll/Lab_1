import xml.etree.ElementTree as ET
import sys
from pprint import pprint

if __name__ == '__main__':
	print('Lab 01 | Problem 2')
	
	parsedBooks = None
	try:
		parsedBooks = ET.parse('Books.xml').getroot()
	except IOError as e:
		print "Failed: %s" %e
		sys.exit()

	booksList = []

	for book in parsedBooks.findall('book'):
		#retrieve information from xml
		bookID = book.get('id')
		author = book.find('author').text
		title = book.find('title').text
		genre = book.find('genre').text
		price = book.find('price').text
		publishDate = book.find('publish_date').text
		description = book.find('description').text

		bookTuple = [bookID,author,title,genre,price,publishDate,description]
		booksList.append(bookTuple)
		
	pprint(booksList)
