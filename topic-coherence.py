import csv
import gensim
from gensim.models import CoherenceModel
from gensim.corpora import Dictionary
from gensim.models import LdaModel

# Combine the preprocessed documents from CSV files
combined_data = []
for year in range(2014, 2024):
    filename = f'{year}.csv'
    try:
        with open(filename, 'r', newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            # Skip the header row if it exists
            header = next(reader, None)
            for row in reader:
                # Skip empty rows
                if not row:
                    continue
                # Get the preprocessed words from the row
                preprocessed_words = row[0].split()  # Assuming words are already preprocessed and separated by whitespace
                combined_data.append(preprocessed_words)
    except FileNotFoundError:
        print(f"{filename} not found.")

# Create a dictionary from the preprocessed documents
dictionary = Dictionary(combined_data)

# Convert the dictionary into a bag-of-words corpus
corpus = [dictionary.doc2bow(doc) for doc in combined_data]

# Function to compute topic coherence
def compute_coherence_values(dictionary, corpus, texts, k):
    lda_model = LdaModel(corpus=corpus, id2word=dictionary, num_topics=k)
    coherence_model = CoherenceModel(model=lda_model, texts=texts, dictionary=dictionary, coherence='u_mass')
    return coherence_model.get_coherence()

# Calculate coherence scores for different numbers of topics
min_topics = 2
max_topics = 10
coherence_scores = []
for num_topics in range(min_topics, max_topics + 1):
    coherence_score = compute_coherence_values(dictionary=dictionary, corpus=corpus, texts=combined_data, k=num_topics)
    coherence_scores.append(coherence_score)

# Find the optimal number of topics based on coherence scores
optimal_num_topics = coherence_scores.index(max(coherence_scores)) + min_topics

print("Optimal number of topics:", optimal_num_topics)
