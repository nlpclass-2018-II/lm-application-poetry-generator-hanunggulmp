import nltk
import collections, nltk
from nltk.util import ngrams
from nltk.corpus import brown
from nltk.probability import LidstoneProbDist, WittenBellProbDist

file = open('Khairil.txt')
text = file.read()
token = nltk.word_tokenize(text)

file2 = open('Poetry.txt')
text2 = file2.read()
testset = nltk.word_tokenize(text2)

def unigram(tokens):
    model = collections.defaultdict(lambda: 0.01)
    for f in tokens:
        try:
            model[f] += 1
        except KeyError:
            model [f] = 1
            continue
    for word in model:
        model[word] = model[word]/float(sum(model.values()))
    return model

def perplexity(testset, model):
    perplexity = 1
    N = 0
    for word in testset:
        N += 1
        perplexity = perplexity * (1/model[word])
    perplexity = pow(perplexity, 1/float(N))
    return perplexity


model = unigram(token)
print(perplexity(testset, model))

result = open('Perplexity Result.txt','w')
result.write('The Perplexity of the Khairils poem and Poetry test is: '+ str(perplexity(testset, model)))