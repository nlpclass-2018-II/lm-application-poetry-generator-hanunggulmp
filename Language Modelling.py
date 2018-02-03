from nltk.collocations import *
from operator import itemgetter
from nltk import RegexpTokenizer

tokenizer = RegexpTokenizer(r'(\w+)') #filter the coma, period, exclamation, etc
input = open('Khairil.txt')
output = open('Revised Number 1 and 2.txt','w')
text = input.read()
token = tokenizer.tokenize(text.lower()) #get all text become lower case
input.close()

#method to merge 2 poetries
def mergePoem(tokens1,tokens2):
    input = open(tokens2)
    text = input.read()
    tokens1 += tokenizer.tokenize(text.lower())
    input.close()
    return tokens1

mergedTokens = mergePoem(token,'Sapardi.txt')
print(mergedTokens)
########################### UNIGRAM ##############################
unigramCount = {}

#counting unigram words
for word in mergedTokens:
    if word in unigramCount:
        unigramCount[word] += 1
    else:
        unigramCount[word] = 1

print(unigramCount)

topTenUni = dict(sorted(unigramCount.items(),key=itemgetter(1), reverse=True)[:10])

print(topTenUni)

output.write('Unigram : ' + str(unigramCount) + '\n')
output.write('Unigram Top 10: ' + str(topTenUni) + '\n' + '\n')

######################################################################################
########################### BIGRAM ##############################

#Counting bigram words

print('\n\n\n','BIGRAM')
bigrams = {}
finder = BigramCollocationFinder.from_words(mergedTokens, window_size = 2)
n = list(finder.ngram_fd.items())
bigrams = n.sort(key=lambda item: item[-1], reverse=True) #creator of bigram variable
print(n)

bigramCount = {}
length = len(mergedTokens)
for word in range(0,length - 1):
    if mergedTokens[word] in bigramCount:
        if mergedTokens[word+1] in bigramCount[mergedTokens[word]]:
            bigramCount[mergedTokens[word]][mergedTokens[word + 1]] += 1
        else:
            bigramCount[mergedTokens[word]][mergedTokens[word + 1]] = 1
    else:
        bigramCount[mergedTokens[word]] = {}
        bigramCount[mergedTokens[word]][mergedTokens[word + 1]] = 1

output.write('Bigram : ' + str(n))
