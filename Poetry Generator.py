import nltk
import random
from nltk.util import ngrams
input = open('Poetry.txt')
text = input.read()
token = nltk.word_tokenize(text)
# NLTK shortcuts :)
bigrams = nltk.bigrams(token)
cfd = nltk.ConditionalFreqDist(bigrams)

#Open output file
result = open('Poetry_Result.txt','w')
# pick a random word from the corpus to start with
word = random.choice(token)
# generate 15 more words
result.write("Poetry Generator from 15 random words: " + word + ' ')
for i in range(15):
    print(word)
    if word in cfd:
        word = random.choice(list(cfd[word].keys()))
        result.write(word + ' ')
    else:
        break

