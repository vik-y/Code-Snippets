from simplecrypt import encrypt, decrypt
import sys

def encrypt_text(text, password):
	return encrypt(password, text)


def decrypt_text(text, password):
	return decrypt(password, text)


def main():
	try:
		inputfilename = sys.argv[3]
		mode = sys.argv[1]
		password = sys.argv[2]
		outputFilename = sys.argv[4]

	except:
		print "Usage: encrypt.py 1-encrypt/2-decrypt password filename output_file_name"
		sys.exit()		
	
	print mode
	if(mode=="1"):
		print "Encryption Called"
		f = open(sys.argv[3], 'r')
		text = f.read()
		f.close()

		out = open(outputFilename, 'w')

		encrypted = encrypt_text(text, password)
		out.write(encrypted)
		out.close()

	if(mode=="2"):
		print "Decryption Called"
		f = open(sys.argv[3], 'r')
		text = f.read()
		f.close()

		out = open(outputFilename, 'w')

		decrypted = decrypt_text(text, password)
		out.write(decrypted)
		
		out.close()	

main()
