import nltk
import os
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

example_sentence = str(input("Key : "))

stop_words = set(stopwords.words('english'))

words = word_tokenize(example_sentence)

print(words)

z = [word for word in words if not word in stop_words]
y = [word for word in stop_words if word in words]

os.system('clear')

print('Number of words out of the stopwords : {}.'.format(len(z)))
print('Number of words within the stopwords : {}.'.format(len(y)))


