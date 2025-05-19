import pandas as pd
import numpy as np
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from tqdm import tqdm
import nltk

# Download VADER lexicon if not already present
nltk.download('vader_lexicon')

# Load comments CSV
df = pd.read_csv("data/youtube_comments.csv")

# Initialize VADER sentiment analyzer
analyzer = SentimentIntensityAnalyzer()

# Show progress during processing
tqdm.pandas(desc="Analyzing Sentiment")

# Compute sentiment compound score for each comment
df['vader_compound'] = df['Comment'].progress_apply(
    lambda text: analyzer.polarity_scores(str(text))['compound']
)

# Classify comments as Positive, Negative, or Neutral
def classify_sentiment(score):
    if score >= 0.05:
        return "positive"
    elif score <= -0.05:
        return "negative"
    else:
        return "neutral"

df['vader_sentiment'] = df['vader_compound'].apply(classify_sentiment)

# Add jitter column for better visualization in scatterplots
df['jitter'] = np.random.uniform(0, 1, len(df))

# Save output CSV
output_file = "data/youtube_comments_with_sentiment.csv"
df.to_csv(output_file, index=False)

print(f"✅ Sentiment analysis complete. Saved to '{output_file}'")
