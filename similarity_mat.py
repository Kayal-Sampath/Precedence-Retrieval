#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 21 07:46:21 2018

@author: kayal
"""

import pandas as pd
import numpy as np
import nltk
import string
from collections import Counter
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import os

path = "/home/kayal/Desktop/a.txt"
token_dict = {}
stemmer = PorterStemmer()

def tokenize(text):
   tokens = nltk.word_tokenize(text)
   stems = stem_tokens(tokens, stemmer)
   return stems

def stem_tokens(tokens, stemmer):
    stemmed_words = []
    for token in tokens:
        stemmed_words.append(stemmer.stem(token))
    return stemmed_words
"""
for subdir, dirs, files in os.walk(path):
    for file in files:
        file_path = subdir + os.path.sep + file
        with open(file_path, "r", encoding = "utf-8") as file:
            story = file
            text = story.read()
            lowers = text.lower()
            map = str.maketrans('', '', string.punctuation)
            no_punctuation = lowers.translate(map)
            token_dict[file.name.split("\\", 1)[1]] = no_punctuation
"""
tfidf = TfidfVectorizer(tokenizer=tokenize, stop_words='english')
tfs = tfidf.fit_transform(token_dict.values())
termarray = tfs.toarray()
nparray = np.array(termarray)
rows, cols = nparray.shape
similarity = []
docdict=[]
for document in docdict:
   for row in range(0, rows-1):
      similarity = cosine_similarity(tfs[row:row+1], tfs)
      docdict[document] = similarity
      
sim = cosine_similarity(tfs)
      
df = pd.DataFrame(sim,columns=list(token_dict.keys()),
                            index=list(token_dict.keys()))

df.to_dict()