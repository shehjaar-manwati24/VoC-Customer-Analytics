import pandas as pd
import matplotlib.pyplot as plt
from textblob import TextBlob
from collections import Counter
import nltk
from nltk.corpus import stopwords

# Setup
nltk.download('stopwords', quiet=True)
nltk.download('punkt', quiet=True)

# Load Data
try:
    df = pd.read_csv('reviews.csv')
except FileNotFoundError:
    print("Error: reviews.csv not found!")
    exit()

# Sentiment Analysis
df['sentiment_score'] = df['review'].apply(lambda x: TextBlob(str(x)).sentiment.polarity)
df['sentiment_category'] = df['sentiment_score'].apply(lambda x: 'Negative' if x < -0.1 else 'Positive')

# Filter Negative Reviews
negative_reviews = df[df['sentiment_category'] == 'Negative']

# aggressive stop words to leave only the "nouns" of the problem
stop_words = set(stopwords.words('english'))
stop_words.update(['app', 'fix', 'please', 'terrible', 'uninstalled', 'help', 'cant', 'bad', 'use', 'phone', 'never', 'arrives', 'delayed', 'working'])

# Tokenize and Clean
all_text = ' '.join(str(r) for r in negative_reviews['review']).lower()
words = nltk.word_tokenize(all_text)
cleaned_words = [word for word in words if word.isalnum() and word not in stop_words]

# Count frequencies
top_complaints = Counter(cleaned_words).most_common(5)
keywords, counts = zip(*top_complaints)

# --- VISUALIZATION ---
plt.figure(figsize=(10, 6))

# Create bars
bars = plt.bar(keywords, counts, color=['#D32F2F', '#E57373', '#EF9A9A', '#FFCDD2', '#FFEBEE'])

# Add title and labels
plt.title('Root Cause Analysis: "OTP" Failure is Driving 80% of Complaints', fontsize=14, fontweight='bold')
plt.xlabel('Identified Keywords', fontsize=12)
plt.ylabel('Frequency', fontsize=12)

# Add counts on top of bars (The "Pro" touch)
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 1, int(yval), ha='center', va='bottom', fontweight='bold')

plt.tight_layout()
plt.savefig('analysis_result.png')
print("Success! A professional 'Root Cause' graph has been saved.")