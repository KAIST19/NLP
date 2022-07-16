from nltk.tokenize import word_tokenize
from collections import Counter

text = input("input text: ")
tokens = word_tokenize(text)

print(Counter(tokens))