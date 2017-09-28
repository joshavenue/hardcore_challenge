import os
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import PlaintextCorpusReader
from collections import Counter

corpus_root = input('PATH directory : ')

file_1 = input('Key file name : ')
file_2 = input('Key file name : ')

with open(file_1) as f1:
	f_1 = f1.read()

with open(file_2) as f2:
	f_2 = f2.read()

wordlists = PlaintextCorpusReader(corpus_root, file_1, file_2)

token_f1 = word_tokenize(f_1)
token_f2 = word_tokenize(f_2)

combo = token_f1 + token_f2

unique_word = [a for a,b in Counter(combo).items() if not b>1]

unique_dist = (len(unique_word) / len(combo) * 100)

print('There are {} unique words exists. '.format(len(unique_word)))
print('{}%  occurence rate.'.format(unique_dist))
