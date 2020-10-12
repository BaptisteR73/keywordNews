from collections import OrderedDict
import re

def extractWords(text):
	keywords = OrderedDict()
	listUrl = {}
	listOfWords = []

	# On parcourt tous le retour Json
	for i in range(len(text)):
		url = text[i]['url']
		title = text[i]['title']
		description = text[i]['description']
		content = text[i]['content']

		# On concatène tous les string que l'on va analyser
		textToAnalyze = str(title) + ' ' + str(description) + ' ' + str(content)
		# Appel de la fonction pour 'nettoyer' les données à analyser
		listOfWords = normalizeWords(textToAnalyze)
		for word in listOfWords :
			if word not in keywords:   # Pour chaque mort
				keywords[word] = 1     # On initialise un compteur à 1
				listUrl[word] = [url]  # On initialise un tableau d'url

			else :
				keywords[word] +=1
				if(url  not in listUrl[word]): # Si l'url n'est pas présente dans le tableau, on l'ajoute
					listUrl[word].append(url)

	sortedKeyWord = sorted(keywords.items(), key=lambda x: x[1], reverse=True) # Tri des mots qui reviennent le plus souvent
	keywords.clear() # On va re créer notre dictionnaire de données
	for y in sortedKeyWord:
		keywords[y[0]] = {       # Pour chaque mot
			'compteur':y[1],     # Son compteur d'apparition
			'url':listUrl[y[0]]  # Sa liste d'URL
		}

	return keywords

# Charge une liste de mot 'inutile' d'un fichier .txt
def loadUselessWords():
	uselessWords = []
	with open('uselessWords.txt', encoding='utf-8') as f:
		for word in f.readlines():
			word = re.sub("\W","",word)
			uselessWords.append(word)
	return uselessWords

# Nettoie les mots à compter
def normalizeWords(text):
	uselessWords = loadUselessWords()
	normalizeWords = []

	text = re.sub("\W"," ",text) # Enlève tous les caractères qui ne sont pas des mots
	text = re.sub("\d+", " ",text) #Enlève les nombres
	text = text.lower()
	words = re.split("\s",text)
	# On enlève les mots de moins de 2 caractères
	for w in words :
		if(len(w) > 2 and w not in uselessWords):
			normalizeWords.append(w)

	return normalizeWords