import pandas as pd
import nltk
from textblob import TextBlob
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt
import seaborn as sns

# Download necessary data
nltk.download('vader_lexicon')

def analyze_sentiment(file_path):
    sia = SentimentIntensityAnalyzer()
    
    #data
    df = pd.read_csv(file_path, on_bad_lines='skip', engine='python')
    print("Data loaded successfully:")
    print(df.head())

    #function
    def get_vader_sentiment(text):
        score = sia.polarity_scores(str(text))['compound']
        if score >= 0.05: return 'Positive'
        elif score <= -0.05: return 'Negative'
        else: return 'Neutral'

    #analysis
    df['vader_sentiment'] = df['Text'].apply(get_vader_sentiment)
    print(df[['Text', 'vader_sentiment']].head())

    # Plotting
    df['vader_sentiment'].value_counts().plot.pie(autopct='%1.1f%%', startangle=90, figsize=(6,6))
    plt.title('Review Sentiment Distribution')
    plt.ylabel('')
    plt.show()

if __name__ == "__main__":
    analyze_sentiment('reviews.csv')
