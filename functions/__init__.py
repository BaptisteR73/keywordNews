def extractWords(text):
	keywords = {}

	for i in range(len(text)):
		title = text[i]['title']
		description = text[i]['description']
		content = text[i]['content']

		textToAnalyze = str(title) + ' ' + str(description) + ' ' + str(content)
		textSplit = textToAnalyze.split()
		#APPELLE FONCTION NORMALIZE A LA PLACE DU SPLIT
		for word in textSplit :
			if word not in keywords:
				keywords[word] = 1
			else :
				keywords[word] += 1

		sortedKeyWord = sorted(keywords.items(), key=lambda x: x[1], reverse=True)

	loadUselessWords()
	return "ok"

def loadUselessWords():
	uselessWords = []
	with open('uselessWords.txt') as f:
		for word in f.readlines():
			uselessWords.append(word)
	return uselessWords

def normalizeWords(text):
	uselessWords = loadUselessWords()
	normalizeWords = []

	text = re.sub("\W"," ",text) # Enlève tous les caractères qui ne sont pas des mots
	text = re.sub("\d+", " ",text) #Enlève les nombres
	text = text.lower()
	words = re.split("\s",text)
	#for w in words

