import praw
import csv
import string
from langdetect import detect

# Import nltk and stopwords
import nltk
import ssl

# Disable SSL check
try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

nltk.download('stopwords')
from nltk.corpus import stopwords

from nltk.tokenize import word_tokenize
nltk.download('punkt')

nltk.download('words')



# Reddit praw client id
reddit = praw.Reddit (
    client_id = "ViBO9-1UV4i7_T5YxYVoLQ",
    client_secret = "BkcDwbvIgHMTkUnBWYo0hWrmAop64Q",
    user_agent = "NLP",
    username = "noobgemie",
)



# Function to clean text
def clean_text(text):
    # Make lowercase
    text = text.lower()

    # Remove punctuation
    translator = str.maketrans('', '', string.punctuation)
    text = text.translate(translator)

    # Remove stopwords
    all_stopwords = stopwords.words('english')
    text = word_tokenize(text)
    removed_stopwords = [word for word in text if word.lower() not in all_stopwords]

    # Remove non-English words
    words = set(nltk.corpus.words.words())
    filtered_words = [w for w in removed_stopwords if w.lower() in words or not w.isalpha()]

    return ' '.join(filtered_words)



# Query string to search for content
query = 'title:((vr OR ar OR xr OR vr/ar OR vr/ar/xr OR "virtual reality" OR "augmented reality" OR "mixed reality") AND (audio OR binaural OR "ambisonic" OR "spatial audio" OR hrtf))'
# query = 'title:(vr OR ar OR xr OR vr/ar OR vr/ar/xr OR "virtual reality" OR "augmented reality" OR "mixed reality") AND psychedelic'

subreddits = ['virtualreality', 'Oculus', 'SteamVR', 'AR_MR_XR', 'ARKit', 'HoloLens', 'Vive', 'PSVR', 'augmentedreality']

# Find posts that contain keywords in title, then put the title, body and comments into csv file
with open('data.csv', 'w', newline = '', encoding = 'utf-8') as f:
  writer = csv.writer(f)

  for subreddit_name in subreddits:
    subreddit = reddit.subreddit(subreddit_name)
    for submission in subreddit.search(query, sort='relevance', limit=None):
    
        writer.writerow([submission.title])
        writer.writerow([submission.selftext])

        submission.comments.replace_more(limit=None)
        comments = submission.comments.list()
        for comment in comments:
            writer.writerow([comment.body])



# Clean data and put to another file
with open('data.csv', 'r', encoding='utf-8') as input_file, open('clean.csv', 'w', newline='', encoding='utf-8') as output_file:
    # Create CSV reader and writer objects
    reader = csv.reader(input_file)
    writer = csv.writer(output_file)
    # writer.writerow(['Raw', 'Cleaned'])

    # Loop through each row in the input file
    for row in reader:
        # Get the content from the first column of the row
        content = row[0]

        # Clean the content
        cleaned_content = clean_text(content)

        # Write the cleaned content to the output file
        writer.writerow([cleaned_content])
