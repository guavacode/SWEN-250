import fileinput

#set up default values for start, stop, and rna to amino codons
START_CODON = "aug"
STOP_CODONS = ["uaa","uag","uga"]
RNA_TO_AAs = {"aug":"Met","uuu":"Phe", "uuc":"Phe", "uua":"Leu", "uug":"Leu", "cuc":"Leu","cug":"Leu","auu":"Ile", "auc":"Ile", "aua":"Ile", "guu":"Val", "guc":"Val", "gua":"Val", "gug":"Val", "ucu":"Ser", "ucc":"Ser", "uca":"Ser", "ucg":"Ser", "ccu":"Pro", "ccc":"Pro", "cca":"Pro", "ccg":"Pro", "acu":"Thr", "acc":"Thr", "aca":"Thr", "acg":"Thr", "gcu":"Ala", "gcc":"Ala", "gca":"Ala", "gcg":"Ala", "uau":"Tyr", "uac":"Tyr", "cau":"His", "cac":"His", "caa":"Gln", "cag":"Gln", "aau":"Asn", "aac":"Asn", "aaa":"Lys", "aag":"Lys", "gau":"Asp", "gac":"Asp", "gaa":"Glu", "gag":"Glu", "ugu":"Cys", "ugc":"Cys", "ugg":"Trp", "cgu":"Arg", "cgc":"Arg", "cga":"Arg", "cgg":"Arg", "agu":"Ser", "agc":"Ser", "aga":"Arg", "agg":"Arg", "ggu":"Gly", "ggc":"Gly", "gga":"Gly", "ggg":"Gly" }

#get input into a string
for inputLine in fileinput.input():
	#by default the start codon hasnt been found
	started = False
	#make the input string all lowercase to match the dicts it will be comparing itself to
	inputLine = inputLine.lower()
	#set the current codon to nothing (it will be built later)
	currentCodon = ""
	#loop through every characters in the input string
	for char in inputLine:
		#if the character is valid
		if (char in ['a','u','c','g']):
			#add the current character to the current codon
			currentCodon += char
			#if the current codon is 3 chars long
			if len(currentCodon) == 3:
				#check if stop codon and set variable
				if currentCodon in STOP_CODONS:
					started = False
				#check if start codon and set variable
				if currentCodon == START_CODON:
					started = True
				#if the start codon has been activated already and the stop hasn't
				if started == True:
					#convert current codon to amino acid and print it
					print(RNA_TO_AAs[currentCodon] + " ", end = " ")
				#reset the current codon string
				currentCodon = ""
