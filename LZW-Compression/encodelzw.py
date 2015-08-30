from utilityFunctions import *
dictionaryLimit = 2**16

#Dictionary can't exceed the above size 


def buildCharacterSet():
	'''
	This function builds the initial character set required for the dictionary
	and returns the dictionary as well as the number of elements in the dictionary
	
	This build a character set of 128 characters.  
	'''
	charSet = {}
	for i in range(0, 128):
		charSet[chr(i)]=i #This builds e.g "a" : 97, "b":98 etc 

	return charSet, 127 

def encode(inputfile, outputfile):
	f = open(inputfile, 'r')
	print "Encoding "
	
	dictionary, numElements = buildCharacterSet() #Building up the initial character set
	#numElements is the number of characters present in the dictionary at the time of generation 
	'''
	p -> previous character
	c -> present character 
	w -> p+c 
	code -> A list to which output is appended 
	'''
	string = f.read()+'c' 
	# Adding one extra character 'c' to make things easy
	p = ''
	code = []
	for c in string:
		w = p+c
		if w in dictionary:
			p = p+c
		else:
			if p!='':
				code.append(dictionary[p])
			if numElements<dictionaryLimit -1:
				# This segment will execute only if we haven't 
				# exceeded the dictionaryLimit. 
				# If our dictionary is full then we can't add
				# any more key,values to it
				dictionary[w] = numElements +1 
				numElements+=1 
			p = c
	
	writeBinaryToFile(outputfile, code)
	# Writing the code into a binary file so that it can be read again 
	# and decoded.
	# NOTE: Please refer to writeBinaryToFile() function in Appendix 1 
	# to understand how exactly it is done. This will save a lot of space
	# when we are writing to a file. 
	return code

if __name__ == "__main__":
	inputFile = sys.argv[1]
	outputFile = sys.argv[2]
	encode(inputFile, outputFile)


