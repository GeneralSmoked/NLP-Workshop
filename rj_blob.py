from pathlib import Path
from textblob import TextBlob
import nltk
from nltk.corpus import stopwords
from wordcloud import WordCloud
import imageio.v2 as imageio


with open('romeoandjuliet.txt', 'r', encoding='utf-8') as f:
    content = f.read()
blob = TextBlob(content)
items = blob.word_counts.items()

stop_words = stopwords.words('english')
filtered_words = [word for word, count in items if word.lower() not in stop_words]

filtered_text = ' '.join(filtered_words)
image_mask = imageio.imread('heart_mask.png')
wordcloud = WordCloud(colormap='prism', mask=image_mask,background_color='white')
wordcloud = wordcloud.generate(filtered_text)
wordcloud = wordcloud.to_file('rj.png')
