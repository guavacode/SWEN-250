import sys

#Count printing function
def printCounts( words ):
	#Print the counts
	print (count_lines(words), count_words(words), count_letters(words), str(sys.argv[1]))
	
	#with open("test.txt", "wt") as out_file:
	#	out_file.write(count_lines(words), count_words(words), count_letters(words, str(sys.argv[1]))

#Word reading function
def readWordsFromFile():
	inputTxt = str(sys.argv[1])
	#Open the file 
	with open ("DarkAndStormyNight.txt", "r") as file:
		#Read file into text variable
		text = file.read()
	#Return file contents
	return text

#Letter counting function
def count_letters( words ):
	#Set counter to 0
	countWord = 0
	#Loop through letters in the words string, incrementing counter by 1
	for c in words:
		countWord += 1
	#Return count of letters
	return countWord

#Line counting funtion
def count_lines( words ):
	#Set counter to 0
	countLine = 0
	#Open the file and loop through lines, incrementing counter by 1
	with open ("DarkAndStormyNight.txt", "r") as file:	
		for line in file:
			countLine += 1
	#Return count of lines
	return countLine

#Word counting function
def count_words( words ):
	#Split string by spaces and return count of words
	return str( len (words.split ()))

#Main program

#Run the printing function
printCounts(readWordsFromFile())
