import nltk
from nltk.collocations import *

class PhrasePhinder() :

	def AnalyzeText(self, text) :
		bigram_measures = nltk.collocations.BigramAssocMeasures()
		trigram_measures = nltk.collocations.TrigramAssocMeasures()

		# change this to read in your data
		tokens = nltk.wordpunct_tokenize(text)
		finder = BigramCollocationFinder.from_words(tokens)

		# only bigrams that appear 3+ times
		finder.apply_freq_filter(3) 

		# return the 10 n-grams with the highest PMI
		return finder.nbest(bigram_measures.pmi, 10)  