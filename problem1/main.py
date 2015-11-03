import os
import sys

def createDeamon():
	print("Creating deamon")
	try:
		pid = os.fork()
	except OSError,e:
	 	raise Exception, "%s [%d]" % (e.strerror,e.errno)


if __name__ == "__main__":
	print("Lab 01")
	createDeamon()
