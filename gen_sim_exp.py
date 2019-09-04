#example
import gensim
import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

from gensim.summarization import summarize
from gensim.summarization import keywords

text = "Thomas A. Anderson is a man living two lives. By day he is an " + \
    "average computer programmer and by night a hacker known as " + \
    "Neo. Neo has always questioned his reality, but the truth is " + \
    "far beyond his imagination. Neo finds himself targeted by the " + \
    "police when he is contacted by Morpheus, a legendary computer " + \
    "hacker branded a terrorist by the government. Morpheus awakens " + \
    "Neo to the real world, a ravaged wasteland where most of " + \
    "humanity have been captured by a race of machines that live " + \
    "off of the humans' body heat and electrochemical energy and " + \
    "who imprison their minds within an artificial reality known as " + \
    "the Matrix. As a rebel against the machines, Neo must return to " + \
    "the Matrix and confront the agents: super-powerful computer " + \
    "programs devoted to snuffing out Neo and the entire human " + \
    "rebellion. "

#print('Input text:')
#print(text)

#To summarize this text, we pass the raw string data as input to
#the function "summarize", and it will return a summary.

print('summary:')
#print(summarize(text))

#Use the "split" option if you want a list of strings instead of a single string.

#print(summarize(text, split=True))

#You can adjust how much text the summarizer outputs via the "ratio" parameter or the "word_count" parameter.
#Using the "ratio" parameter, you specify what fraction of sentences in the original text should be returned as output.
#Below we specify that we want 50% of the original text (the default is 20%).

#print(summarize(text, ratio=0.5))

#Using the "word_count" parameter, we specify the maximum amount of words we want in the summary.
#print(summarize(text, word_count=50))

#keywords
print(keywords(text))
