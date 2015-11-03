import xml.etree.ElementTree

if __name__ == "__main__":
	print("Lab 01 | Problem 2")
	
	parsedBooks = xml.etree.ElementTree.parse('Books.xml').getroot()
	booksList = []
	for book in parsedBooks.findall('book'):
		bookID = book.get('id')
		author = book.find('author').text
		title = book.find('title').text
		genre = book.find('genre').text
		price = book.find('price').text
		bookTuple = [bookID,author]
		booksList.append(bookTuple)
		
	print(booksList)
