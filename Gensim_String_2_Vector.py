#Gensim
#Corpa_Vector_Spaces
import gensim
import logging
from gensim import corpora

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

#Nine documents, all one sentence

documents = ["Human machine interface for lab abc computer applications",
              "A survey of user opinion of computer system response time",
              "The EPS user interface management system",
              "System and human system engineering testing of EPS",
              "Relation of user perceived response time to error measurement",
              "The generation of random binary unordered trees",
              "The intersection graph of paths in trees",
              "Graph minors IV Widths of trees and well quasi ordering",
              "Graph minors A survey"]

#Tokenize the documents, remove common words, remove one time appearence

from pprint import pprint  # pretty-printer
from collections import defaultdict

# remove common words and tokenize
stoplist = set('for a of the and to in'.split())
texts = [
     [word for word in document.lower().split() if word not in stoplist]
     for document in documents
]

# remove words that appear only once
frequency = defaultdict(int)
for text in texts:
    for token in text:
         frequency[token] += 1

texts = [
     [token for token in text if frequency[token] > 1]
     for text in texts
]

dictionary = corpora.Dictionary(texts)
# store the dictionary, for future reference
dictionary.save('/tmp/deerwester.dict')  

#print(dictionary.token2id)

new_doc = "Human computer interaction"
new_vec = dictionary.doc2bow(new_doc.lower().split())
# the word "interaction" does not appear in the dictionary and is ignored
print(new_vec)

