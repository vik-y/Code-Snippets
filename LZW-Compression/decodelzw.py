from utilityFunctions import *
dictionaryLimit = 2**16

def decode(encodedFile, decodedFile):
	print "Decoding"
	'''
	cW -> Received code word
	pW -> previous Word 
	'''
	encodedInput = readFromFile(encodedFile)
	output = ''
	numElements = 127 
	dictionary = {}
	
	for i in range(0, 128):
		# Generating dictionary for decoding. 
		# Reversed order to make lookup faster O(1)
		dictionary[i] = chr(i)
		dictionary[chr(i)] = i
	
	output += dictionary[encodedInput[0]]
	pW = encodedInput[0]
	i = 0
	for cW in encodedInput[1:]:
		#print dictionary[cW]
		#print i
		if cW in dictionary:
			# If current word is in dictionary
			temp = dictionary[cW]
			#print temp
			output += temp
			P = dictionary[pW]
			C = temp[0]
			if numElements<dictionaryLimit:
				# This segment will execute only if we haven't 
				# exceeded the dictionaryLimit. 
				# If our dictionary is full then we can't add
				# any more key,values to it
				dictionary[numElements+1] = P+C
				numElements +=1
			pW = cW
		else:
			#If current word is not in dictionary
			P = dictionary[pW]
			C = dictionary[pW][0]
			#print P+C
			output = output+P+C
			if numElements<dictionaryLimit:
				# This segment will execute only if we haven't 
				# exceeded the dictionaryLimit. 
				# If our dictionary is full then we can't add
				# any more key,values to it
				dictionary[numElements+1] = P+C
				numElements+=1
			pW = numElements
		i+=1
	#print output[:-1]
	writeTextToFile(decodedFile, output)
	#Writing the output to a text file
	
	sizeOfText = len(output)*7
	sizeOfCompressedArray = len(encodedInput)*16
	
	compressionRatio = float(sizeOfText)/sizeOfCompressedArray
	print "Compression Ratio", compressionRatio

if __name__=="__main__":
	encodedFile = sys.argv[1]
	decodedFile = sys.argv[2]
	decode(encodedFile, decodedFile)

