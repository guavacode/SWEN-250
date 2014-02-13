import sys

def roman(entered):
	print(entered)
	# the enciphered string to return 
	enciphered = ''
   
	# traverse the entered string and create an enciphered string
	for char in entered:
		#if the char is in the alphabet
		if char.isalpha():
			#if the char is uppercase
			if char.isupper():
				#if the char is in the last half of the alphabet
				if ord(char) >= 78:
					#have the char go back 13 characters
					enciphered += chr(ord(char)-13)
				#if the char is in the first half of the alphabet
				elif ord(char) < 78:
					#have the char go forward 13 characters
					enciphered += chr(ord(char)+13)
			#if the char is lowercase
			elif char.islower():
				#if the char is in the last half of the alphabet
				if ord(char) >= 110:
					#have the char go back 13 characters
					enciphered += chr(ord(char)-13)
				#if the char is in the first half of the alphabet
				elif ord(char) < 110:
					#have the char go forward 13 characters
					enciphered == chr(ord(char)+13)
		#otherwise (if not in the alphabet)
		else:
			#simply add the char to the string
			enciphered += char
	#return the string
	return enciphered

def main():
	#get input and stick it in the string with garbage values stripped
	for line in sys.stdin:
		line = line.rstrip()
	#print the ciphered string
	print(roman(line))

main()
