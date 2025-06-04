from textblob import TextBlob
import nltk
from textblob.sentiments import NaiveBayesAnalyzer


text = 'Today is a beautiful day. Tomorrow looks like a bad weather.'
blob = TextBlob(text, analyzer=NaiveBayesAnalyzer())

print(blob.sentiment)



