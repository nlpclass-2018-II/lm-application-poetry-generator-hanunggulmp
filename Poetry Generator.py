import nltk
import math
import random
from nltk.tokenize import RegexpTokenizer

tokenizer = RegexpTokenizer(r'(\w+)') #filter the coma, period, exclamation, etc

input = open('Poetry.txt')
text = input.read()


def mergePoem(tokens,tokens2):
    input=open(tokens)
    text = input.read()
    tokens = tokenizer.tokenize(text.lower())
    input.close()
    input = open(tokens2)
    text = input.read()
    tokens += tokenizer.tokenize(text.lower())
    input.close()
    mergedTokens = tokens
    return mergedTokens

token = mergePoem('Khairil.txt','Sapardi.txt')
print(token)


# NLTK shortcuts :)
bigrams = nltk.bigrams(token)
cfd = nltk.ConditionalFreqDist(bigrams)

#Open output file
result = open('Poetry_Result.txt','w')

# pick a random word from the corpus to start with
word = random.choice(token)
print(cfd[word].keys())
result.write("Poetry Generator from 15 random words: \n" + word + ' ')
print(word)
# generate 15 more words
wordused = []
print(cfd)
for i in range(20):
    if (word in cfd) & (word not in wordused): #iterate the tokens without repeating the same word
        wordused.append(word)
        word = random.choice(list(cfd[word].keys())) #choose a random word that has a high frequence
        result.write(word + ' ')
    else:
        break
print('wordused:',wordused)
print('prob:',list(cfd[word]))
