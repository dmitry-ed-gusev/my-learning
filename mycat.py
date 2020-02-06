import sys

text = len(sys.argv)

if text > 1:

	text = open(sys.argv [1])

	print (text.read())
else:
	print ("Plesase provide a file for printing...")