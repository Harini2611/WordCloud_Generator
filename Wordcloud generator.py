#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Harini Rajarathinam
#Wordcloud generator


# In[76]:


import re
import nltk
nltk.download('punkt')
from nltk.corpus import stopwords
from nltk.probability import FreqDist
from nltk.tokenize import word_tokenize
import matplotlib.pyplot as plt
from wordcloud import WordCloud


# In[77]:


# Load the text data
with open(r"C:\Users\rcher\Documents\Important docs\My Data Analytics projects & certificates\datasets\alice.txt", 'r') as f:
    text = f.read()


# In[83]:


# Tokenize the text
tokens = nltk.word_tokenize(text)

# Remove stop words
stop_words = set(stopwords.words('english'))
filtered_tokens = [token for token in tokens if token.lower() not in stop_words]

# Compute word frequencies
word_freq = nltk.FreqDist(filtered_tokens)

# Create frequency distribution and remove common words
freq_dist = FreqDist(tokens)
common_words = [word for word, count in freq_dist.most_common(10)]
tokens = [token for token in tokens if token not in common_words]


# In[84]:


# Generate word frequencies
word_freq = {}
for word in text.split():
    if word not in word_freq:
        word_freq[word] = 0
    word_freq[word] += 1


# In[85]:


# Generate word cloud
wordcloud = WordCloud(width=800, height=800, background_color='black', colormap='plasma').generate_from_frequencies(word_freq)


# In[86]:


# Display the generated image:
plt.figure(figsize=(8,8))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()

