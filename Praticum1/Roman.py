import sys

def roman(entered):
	print(entered)
	# the enciphered string to return 
	enciphered = ''
   
	# traverse the entered string and create an enciphered string
	for char in entered:
		if char.isalpha():
			if char.isupper():
				if ord(char) >= 78:
					enciphered += chr(ord(char)-13)
				elif ord(char) < 78:
					enciphered += chr(ord(char)+13)
			elif char.islower():
				if ord(char) >= 110:
					enciphered += chr(ord(char)-13)
				elif ord(char) < 110:
					enciphered == chr(ord(char)+13)
		else:
			enciphered += char
	return enciphered

def main():
	for line in sys.stdin:
		line = line.rstrip()
	print(roman(line))

main()
