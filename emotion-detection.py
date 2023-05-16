from transformers import pipeline
import csv
import matplotlib.pyplot as plt

classifier = pipeline("text-classification", model="j-hartmann/emotion-english-distilroberta-base", top_k=None, max_length=512, truncation=True)



# Calculate most expressed emotion

# Function to calculate the highest emotion score for a row
def calculate_highest_emotion(sentence):
    # Get the emotion scores for the row
    scores_list = classifier(sentence)

    # Find the emotion with the highest score
    highest_emotion = max(scores_list[0], key=lambda x: x['score'])
    return highest_emotion['label']

def emotion_percentages(file_path):
    # Initialize dictionaries to hold the total counts for each emotion
    emotion_counts = {
        "anger": 0,
        "disgust": 0,
        "fear": 0,
        "joy": 0,
        "neutral": 0,
        "sadness": 0,
        "surprise": 0,
    }

    # Initialize a counter for the total number of rows
    total_rows = 0

    # Open the CSV file and read the rows
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        # Skip the header row if it exists
        header = next(reader, None)

        # Loop through each row in the CSV file
        for row in reader:
            # Skip empty rows
            if not row:
                continue

            # Get the sentence from the row
            sentence = row[0]

            # Calculate the highest emotion score for the row
            highest_emotion = calculate_highest_emotion(sentence)

            # Increment the count for the highest emotion
            emotion_counts[highest_emotion] += 1

            # Increment the total number of rows
            total_rows += 1

    # Calculate the percentage of each emotion
    emotion_percentages = {}
    for emotion, count in emotion_counts.items():
        percentage = count / total_rows * 100 if total_rows > 0 else 0
        emotion_percentages[emotion] = percentage
    
    #Print the percentage of each emotion
    for emotion, percentage in emotion_percentages.items():
        print(f"{emotion}: {percentage:.2f}%")

    # Create a bar chart from the emotion percentages
    emotions = list(emotion_percentages.keys())
    percentages = list(emotion_percentages.values())

    fig, ax = plt.subplots()
    ax.bar(emotions, percentages, color=['red', 'green', 'purple', 'blue', 'gray', 'orange', 'pink'])

    ax.set_title(f'Emotion Percentages - {file_path}')
    ax.set_xlabel('Emotion')
    ax.set_ylabel('Percentage')

    plt.show()

for year in range(2014, 2024):
  filename = f'{year}.csv'
  emotion_percentages(filename)
  


# Calculate emotion in total
def combine_csv_files():
    combined_rows = []

    for year in range(2014, 2024):
        filename = f'{year}.csv'

        try:
            with open(filename, 'r', newline='', encoding='utf-8') as csvfile:
                reader = csv.reader(csvfile)
                # Skip the header row if it exists
                header = next(reader, None)
                combined_rows.extend(reader)
        except FileNotFoundError:
            print(f"{filename} not found.")

    return combined_rows

def calculate_emotion_percentages(combined_rows):
    # Initialize dictionaries to hold the total counts for each emotion
    emotion_counts = {
        "anger": 0,
        "disgust": 0,
        "fear": 0,
        "joy": 0,
        "neutral": 0,
        "sadness": 0,
        "surprise": 0,
    }

    # Initialize a counter for the total number of rows
    total_rows = 0

    # Loop through each row in the combined data
    for row in combined_rows:
        # Skip empty rows
        if not row:
            continue

        # Get the sentence from the row
        sentence = row[0]

        # Calculate the highest emotion score for the row
        highest_emotion = calculate_highest_emotion(sentence)

        # Increment the count for the highest emotion
        emotion_counts[highest_emotion] += 1

        # Increment the total number of rows
        total_rows += 1

    # Calculate the percentage of each emotion
    emotion_percentages = {}
    for emotion, count in emotion_counts.items():
        percentage = count / total_rows * 100 if total_rows > 0 else 0
        emotion_percentages[emotion] = percentage

    return emotion_percentages

# Combine the CSV files
combined_data = combine_csv_files()

# Calculate the emotion percentages
emotion_percentages = calculate_emotion_percentages(combined_data)

# Print the emotion percentages
for emotion, percentage in emotion_percentages.items():
    print(f"{emotion}: {percentage:.2f}%")



# Calculate average score of 7 emotions

# def calculate_average_emotions(file_path):
#     # Initialize dictionaries to hold the total scores for each emotion
#     emotions_total = {
#         "anger": 0,
#         "disgust": 0,
#         "fear": 0,
#         "joy": 0,
#         "neutral": 0,
#         "sadness": 0,
#         "surprise": 0,
#     }
#     # Initialize a dictionary to hold the count of sentences
#     sentence_count = {
#         "anger": 0,
#         "disgust": 0,
#         "fear": 0,
#         "joy": 0,
#         "neutral": 0,
#         "sadness": 0,
#         "surprise": 0,
#     }

#     # Open the CSV file
#     with open(file_path, newline='', encoding='utf-8') as csvfile:
#         reader = csv.reader(csvfile)

#         # Loop through each row in the CSV file
#         for row in reader:
#             # Get the text from the current row
#             if row:
#                 sentence = row[0]

#             # Get the emotion scores for the current sentence
#             scores_list = classifier(sentence)

#             emotion_scores = {}
#             for item in scores_list[0]:
#               emotion_scores[item['label']] = item['score']

#             # Loop through each emotion and add its score to the total
#             for emotion, score in emotion_scores.items():
#               emotions_total[emotion] += score
#               sentence_count[emotion] += 1

#     # Calculate the average score for each emotion
#     average_emotions = {}
#     for emotion, total_score in emotions_total.items():
#         count = sentence_count[emotion]
#         average_emotions[emotion] = total_score / count if count > 0 else 0

#     return average_emotions

# for year in range(2014, 2024):
#   filename = f'{year}.csv'
#   print(filename, calculate_average_emotions(filename))