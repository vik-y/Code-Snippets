import struct, os, sys

def addtoDict(key, value, dictionary):
	'''
	Function to add key value pairs to dictionary 
	'''
	dictionary[key] = value
	
def readFromFile(filename):
	with open(filename, 'rb') as f:
		content = f.read()
		bytes = os.stat(filename).st_size
		
		print "unpacking"  
		unpackLength = bytes/2
		
		h= ''
		for i in range(0, unpackLength):
			h+='H'
   
    	return struct.unpack(h, content)

	
def writeBinaryToFile(filename, binary):
	with open(filename, 'wb') as f:
		for b in binary:
			#print b
			f.write(struct.pack('H', b)) #or whatever format you need
			

def writeTextToFile(filename, text):
	with open(filename, 'w') as f:
		f.write(text)

