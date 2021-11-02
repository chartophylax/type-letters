type1="qwertyuiop"
type2="asdfghjkl"
type3="zxcvbnm"
wordlen1 = 0
wordlen2 = 0
wordlen3 = 0

word = input ("Введите что-то: ")

for i in type1:
	for j in word:
		if i == j:
			wordlen1 += 1

if len(word) == wordlen1:
	print ("Слово", word, "состоит из", type1)
else:
	for i in type2:
		for j in word:
			if i == j:
				wordlen2 += 1
	if len(word) == wordlen2:
		print ("Слово", word, "состоит из", type2)
	else:
		for i in type3:
			for j in word:
				if i == j:
					wordlen3 += 1
		if len(word) == wordlen3:
			print ("Слово", word, "состоит из", type3)
		else:
			print ("The word", word, "is not in", type1, "or", type2, "or", type3)
