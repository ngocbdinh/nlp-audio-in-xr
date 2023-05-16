import pandas as pd
from textblob import TextBlob
import matplotlib.pyplot as plt


# Define a function to compute the polarity score of a text
def get_polarity(text):
    if isinstance(text, float):
        text = str(text)
    blob = TextBlob(text)
    return blob.sentiment.polarity



# Define average polarity in general
def polarity_average(files):
    dfs = []

    # Load the CSV file into a Pandas dataframe
    for file in files:
        df = pd.read_csv(file)
        df['text'] = df['text'].fillna('')
        dfs.append(df)
    
    # Concatenate all DataFrames into one
    combined_df = pd.concat(dfs, ignore_index=True)

    # Extract the text data from the dataframe
    df['polarity'] = combined_df['text'].apply(get_polarity)

    # Count the number of rows with negative, neutral, and positive polarity scores
    negative_count = 0
    neutral_count = 0
    positive_count = 0

    for polarity in df['polarity']:
        if polarity < 0:
            negative_count += 1
        elif polarity == 0:
            neutral_count += 1
        else:
            positive_count += 1

    # Compute the percentage of rows with negative, neutral, and positive polarity scores
    total_count = len(df)
    negative_percentage = negative_count / total_count * 100
    neutral_percentage = neutral_count / total_count * 100
    positive_percentage = positive_count / total_count * 100

    # Create a pie chart of the polarity percentages
    labels = ['Negative', 'Neutral', 'Positive']
    sizes = [negative_percentage, neutral_percentage, positive_percentage]
    colors = ['red', 'gray', 'green']
    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
    ax.set_title(f'Polarity of content - {file}')
    plt.show()

files = []

for year in range(2014, 2024):
  filename = f'{year}.csv'
  files.append(filename)

polarity_average(files)



# Function to define polarity by year
def polarity(file):
    # Load the CSV file into a DataFrame
    df = pd.read_csv(file)

    # Compute the polarity score for each row in the DataFrame
    df['polarity'] = df['text'].apply(get_polarity)

    # Count the number of rows with negative, neutral, and positive polarity scores
    negative_count = 0
    neutral_count = 0
    positive_count = 0

    for polarity in df['polarity']:
        if polarity < 0:
            negative_count += 1
        elif polarity == 0:
            neutral_count += 1
        else:
            positive_count += 1

    # Compute the percentage of rows with negative, neutral, and positive polarity scores
    total_count = len(df)
    negative_percentage = negative_count / total_count * 100
    neutral_percentage = neutral_count / total_count * 100
    positive_percentage = positive_count / total_count * 100

    # Create a pie chart of the polarity percentages
    labels = ['Negative', 'Neutral', 'Positive']
    sizes = [negative_percentage, neutral_percentage, positive_percentage]
    colors = ['red', 'gray', 'green']
    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
    ax.set_title(f'Polarity of content - {file}')
    plt.show()

for year in range(2014, 2024):
  filename = f'{year}.csv'
  with open(filename, 'r', newline='', encoding='utf-8') as file:
    polarity(file)
