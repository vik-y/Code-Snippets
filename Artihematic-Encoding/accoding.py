'''
Arithematic Encoder 
by Vikas Yadav 
IMT2013060 

Please Note that this file won't run without utilityFunctions.py which
should be present in the same folder. 

utilityFunctions.py present in Appendix 1 
'''
import sys
from decimal import Decimal
from utilityFunctions import *

def stringToDecimal(s):
	'''
	A utility function to convert a given binary string to decimal 
	'''
	if(s==''):
		return 0
	total = 0.0;
	length = len(s)
	count = 1
	for i in s:
		val = float(i)/(2**count)
		total += val
		count+=1
	return total;

def decimalToString(d):
	'''
	A utility function to convert a given decimal string to binary 
	'''
	if d==0:
		return '0'
	if(d*2==1):
		return '1'
	elif d*2>1:
		return '1'+decimalToString(d*2-1)
	else:
		return '0'+decimalToString(d*2)

def findRangeFloating(minVal, maxVal, start):
	'''
	Given min and max value of a floating point number, this function 
	returns a string of the smallest binary number in that range 
	'''
	minVal, maxVal = float(minVal), float(maxVal)
	current = stringToDecimal(start+'1')
	#print Decimal(current)
	if current>minVal and current<=maxVal: #note: changed inequality here, different from original function
		return '1'
	elif current > maxVal:
		return '0'+findRangeFloating(minVal, maxVal, start+'0')
	elif current <= minVal:
		return '1'+findRangeFloating(minVal, maxVal, start+'1')


def makeProbabilityRange(filename):
	'''
	This function does the following:
	
	Reads a file <filename> passed as argument
	Generates a probability function for all the ascii values.
	Adjusts the probability range to make the encoding and decoding work
	
	returns the asciiCharacter and adjusted probability associated with it
	'''

	f = open(filename, 'r') #opening file

	dictionary = {}

	for i in range(0, 256): #dictionary size is 256 now
		dictionary[chr(i)] = 0
	
	text = f.read()
	for c in text:
		dictionary[c]+=1 #frequency 
	
	events = [0]
	probability = [0]
	
	total = len(text) #total number of characters in the file
	
	prev = 0
	
	for key, value in dictionary.items():
		# In this loop we are calculating probability of each character
		# and put the cumuluative probability along with the associated
		# event in two different lists, 'probability' and 'events' respectively
		if value!=0:
			events.append(key) #appending the character 
			probability.append(float(value)/total + probability[prev]) #appending the related cumulative probability
			prev+=1
	
	
	for i in range(1, len(probability)):
		# In this loop we are adjusting the probability range so that we
		# do our encoding and decoding easily and optimally 
		temp = stringToDecimal(findRangeFloating(probability[i-1], probability[i], ''))
		probability[i] = temp
	
	probability.append(1)
	
	return events, probability[1:] #returns characters and cumulative frequency table

events, probability = makeProbabilityRange('input.txt') 
d = {}
for i in range(1, len(events)):
	d[events[i]] = (probability[i-1], probability[i])


initialsize = 0

def encodeAc(filename):
	'''
	Arithematic Encoder
	16 bits 
	
	filename : Name of the File to be encoded 
	'''
	print "Decoding text from file ", filename, "\n-------------------------"
	global initialsize
	f = open(filename, 'r')
	text = f.read()+' '
	#Reading the entire file together. Can create problems for large files 
	#But ok for now since we won't have any file greater than 100MB
	#Correct way is to reach chunks
	f.close()
	
	initialsize=len(text)*7
	
	low, high = 0.0, 1
	size = 0
	encodedValues = []
	
	i=0
	while i<len(text):
		c = text[i]
		r = high - low
		#print "Encoding", c
		size = len(decimalToString(low + r*d[c][0]))

		if size>16: #This check is required so that we don't exceed 16 bits limit
			encodedValues.append(low)
			low, high = 0, 1
		else:
			high =  low+r*d[c][1]
			low =  low + r*d[c][0]
			i+=1
		#if(i==len(text)-1):
		#	encodedValues.append(low)
	
	writetofile = []
	
	for i in encodedValues:
		writetofile.append(int(decimalToString(i), 2)) 
		# Write decimal representation of codes in form of integers in a file to save space 
	
	writeBinaryToFile('encodedac.bin', writetofile)
	
	return encodedValues 
	#Return the array of encoded decimal values 
			
def decodeAc(encoded):
	'''
	Arithematic Decoder
	
	encoded: Array of encoded decimal values 
	'''
	lows = encoded
	output = ''
	finalsize = 0 
	
	
	for i in range(0, len(lows)):
		# looping over all the decimal values 
		low = lows[i]
		finalsize+= len(decimalToString(low)) # To calculate total size of encoded decimal values 
		while(low>0):
			#To extract ascii values from decimal
			for i in range(1, len(probability)): # Need to make this part order 1 using dictionary 
				if low < probability[i]:
					symbol = events[i]
					#print symbol	
					output += symbol 
					# Extracted symbol appending to output
					
					#print low, symbol
					r = d[symbol][1]-d[symbol][0] 
					# Calculating the range
					 
					low = low - d[symbol][0] 
					#Subtracting by lower value 
					
					low = low/r 
					#dividing by range 
					break
					
	print output		
	print "Initial size", initialsize, "bits" 
	#NOTE: I multiplied by 7 to calculate number of bits not 8 
	
	print "Final size", finalsize, "bits"	
	#finalsize = float(len(encoded))*16
	print "Compression Ratio", initialsize/float(finalsize) 
	#Compression Ratio = bits before compression / bits after compression 
	

encoded = encodeAc('input.txt')
#print encoded
decodeAc(encoded)
		
