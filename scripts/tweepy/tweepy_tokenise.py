#!/usr/bin/python
from nltk.tokenize import word_tokenize
import re

emoticons_str = r"""
    (?:
        [:=;] #eyes
        [oO\-]?
        [D\)\]\(\]/\\OpP]
    )"""




tweet = 'RT @marcobonzanini: just an example! :D http://example.com #NLP'
print(word_tokenize(tweet))




^[:\)|:\()+%]