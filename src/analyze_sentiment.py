import pandas as pd
from nltk.sentiment import SentimentIntensityAnalyzer
import nltk

nltk.download("vader_lexicon")

def label_sentiment(score):
    if score >= 0.05:
        return "positive"
    elif score <= -0.05:
        return "negative"
    else: 
        return "neutral"
    
def analyze_headlines(headlines):
    sita = SentimentIntensityAnalyzer()
    data = []
    for text in headlines:
        scores = sita.polarity_scores(text)
        data.append({**scores, "text": text})
    df = pd.DataFrame(data)
    df["label"] = df["compound"].apply(label_sentiment)
    return df