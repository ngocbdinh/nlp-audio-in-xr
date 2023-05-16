# NLP: Audio in XR

## Description

### Data
10 CSV files containing social media data retrieved from Reddit related to audio in XR, separated by 10 years from 2014 to 2023.

---

### `frequecy.py`
Calculate the word frequency among 10 CSV files, draw wordcloud, then make a CSV file containing top-40 most common words and their counts correspondingly. 

---

### `polarity.py`
Define the polarity (negative/neutral/positive) of each data line using TextBlob, then calculate the polarity percentage both as a whole and on yearly basis.

---

### `emotion-detection.py`
Define the score of 7 emotions using the huggingface emotion model. The most intense emotion of each post was identified based on emotion score, then put in a dataset to calculate the percentage of each emotion among all posts.

---

### `topic-coherence.py`
Identify the optimal number of topics based on the maximum coherence score using the UMass coherence measure in Gensim.

---

### `topic-modeling.py`
Create topic models using Latent Dirichlet Allocation (LDA).

---


## General usage information

1. Install Python from [python.org](http://www.python.org/downloads/).
2. Download the [ZIP package](https://github.com/ngocbdinh/nlp-audio-in-xr/archive/refs/heads/main.zip) and unzip it.
3. Move all the data files from Data folder to main folder.
4. Run a terminal at main folder.
5. The scripts will run by simply typing `python3 ` followed by the file name of the script, e.g. `frequency.py`.
