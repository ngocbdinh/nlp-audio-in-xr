import csv
from nltk.tokenize import word_tokenize
import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt



# Join csv file into a string
for year in range(2014, 2024):
  filename = f'{year}.csv'
  with open(filename, 'r', newline='', encoding='utf-8') as file:
    reader = csv.reader(file)
    content = ''
    for row in reader:
      content += ','.join(row) + '\n'



# Count frequency and draw wordcloud
def draw_wordcloud(name):
  # Word count
  words_count = {}
  words = word_tokenize(name)
  for word in words:
    if len(word) >= 3:
      if word in words_count.keys():
        words_count[word] += 1
      else:
        words_count[word] = 1
  
  # Put 40 most frequent words and their counts into a file
  df = pd.DataFrame(list(words_count.items()), columns=['word', 'frequency'])
  df = df.sort_values('frequency', ascending=False) 
  df.head(40).to_csv('frequency.csv', index=False)

  # Draw wordcloud
  wordcloud = WordCloud(width = 800, height = 800,
                background_color ='white',
                min_font_size = 10).generate_from_frequencies(words_count)

  plt.figure(figsize = (8, 8), facecolor = None) 
  plt.imshow(wordcloud) 
  plt.axis("off") 
  plt.tight_layout(pad = 0) 
  plt.show() 

draw_wordcloud(content)