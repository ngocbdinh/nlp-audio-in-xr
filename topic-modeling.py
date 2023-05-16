from __future__ import print_function
import pandas as pd
import pyLDAvis
import pyLDAvis.lda_model
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.decomposition import LatentDirichletAllocation



def topic_modeling(files):

    dfs = []

    # Load the CSV file into a Pandas dataframe
    for file in files:
        df = pd.read_csv(file)
        df['text'] = df['text'].fillna('')
        dfs.append(df)
    
    # Concatenate all DataFrames into one
    combined_df = pd.concat(dfs, ignore_index=True)

    # Extract the text data from the dataframe
    text_data = combined_df['text'].tolist()

    # Create a document-term matrix using CountVectorizer
    tf_vectorizer = CountVectorizer()
    dtm_tf = tf_vectorizer.fit_transform(text_data)

    # Create a document-term matrix using TF-IDF Vectorizer
    tfidf_vectorizer = TfidfVectorizer(**tf_vectorizer.get_params())
    dtm_tfidf = tfidf_vectorizer.fit_transform(text_data)

    # Perform LDA on the TF-IDF Vectorizer DTM
    lda_tfidf = LatentDirichletAllocation(n_components=6, random_state=0)
    lda_tfidf.fit(dtm_tfidf)

    # Generate the pyLDAvis visualization for the TF-IDF Vectorizer DTM
    vis_tfidf = pyLDAvis.lda_model.prepare(lda_tfidf, dtm_tfidf, tfidf_vectorizer)
    pyLDAvis.save_html(vis_tfidf, 'lda_visualization.html')

    # Perform LDA on the CountVectorizer DTM
    # lda_tf = LatentDirichletAllocation(n_components=5, random_state=0)
    # lda_tf.fit(dtm_tf)

    # Generate the pyLDAvis visualization for the CountVectorizer DTM
    # vis_tf = pyLDAvis.lda_model.prepare(lda_tf, dtm_tf, tf_vectorizer)
    # pyLDAvis.save_html(vis_tf, 'lda_visualization-tf.html')

files = []

for year in range(2014, 2024):
  filename = f'{year}.csv'
  files.append(filename)

topic_modeling(files)