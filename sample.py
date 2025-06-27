import nltk
nltk.download("vader_lexicon")
from nltk.sentiment import SentimentIntensityAnalyzer

import pandas as pd

headlines = [
    "Stocks rally as inflation fears ease",
    "War in Ukraine causes global concern",
    "New vaccine shows promising results",
    "Natural disaster strikes coastal city",
    "Tech giants face new regulations",
    "Unemployment rate drops significantly",
    "Celebrity couple announces divorce",
    "Scientists discover cure for rare disease",
    "Government approves new economic plan",
    "Major data breach affects millions"
]

sia = SentimentIntensityAnalyzer()

data = []
for text in headlines:
    scores = sia.polarity_scores(text)
    data.append({**scores, "text": text})

print(data)