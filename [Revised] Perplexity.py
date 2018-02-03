import collections, nltk
from nltk import RegexpTokenizer

tokenizer = RegexpTokenizer(r'(\w+)') #filter the coma, period, exclamation, etc

file = open('Poetry.txt')
text = file.read()
testset = nltk.word_tokenize(text)

file2 = open('Khairil.txt')
text2 = file2.read()
train1 = nltk.word_tokenize(text2)

file3 = open('Sapardi.txt')
text3 = file3.read()
train2 = nltk.word_tokenize(text3)

#merge Khairil's and Sapardi's poem into a training data
def mergePoem(train1,train2):
    text2 = tokenizer.tokenize(train1.lower())
    text3 = tokenizer.tokenize(train2.lower())
    tokens = text2
    tokens += text3
    return tokens

trainer = mergePoem(text2,text3)
print(trainer)

#compute the probability of each unigram's word
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

#calculate the perplexity
def perplexity(testset, model):
    perplexity = 1
    N = 0
    for word in testset:
        N += 1
        perplexity = perplexity * (1/model[word])
    perplexity = pow(perplexity, 1/float(N))
    return perplexity


model = unigram(trainer)#model for both poem
model2 = unigram(train1)#model for Khairil's
model3 = unigram(train2)#model for Sapardi's


print(model)
print(model2)
print(model3)

#perplexity between datatest and datatraining)
print('With both of 2 poems:',perplexity(testset, model))
print('With Khairil\'s poem:',perplexity(testset,model2))
print('With Sapardi\'s poem:',perplexity(testset,model3))

result = open('[Revised] Perplexity Result.txt','w')
result.write('With both of 2 poems:'+ str(perplexity(testset, model)))
result.write('With Khairil\'s poem:'+ str(perplexity(testset,model2)))
result.write('With Sapardi\'s poem:'+ str(perplexity(testset,model3)))