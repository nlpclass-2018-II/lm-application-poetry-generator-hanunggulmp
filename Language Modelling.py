import nltk
from nltk import word_tokenize
from nltk.util import ngrams
from collections import Counter

input = open('Khairil.txt')
output = open('Result Number 1 and 2.txt','w')
text = input.read()
token = nltk.word_tokenize(text)

unigram = ngrams(token,1)
bigrams = ngrams(token,2)

uniCounter = Counter(unigram)
biCounter = Counter(bigrams)

print("Unigram: ",str(uniCounter))
print("Bigram : ",str(biCounter))

output.write('Unigram: ' + str(uniCounter) + '\n' + '\n')
output.write('Bigram : ' + str(biCounter))
