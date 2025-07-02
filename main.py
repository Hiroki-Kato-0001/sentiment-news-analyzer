from src.fetch_news import get_headlines
from src.analyze_sentiment import analyze_headlines
from src.visualize import plot_sentiment_distribution

def main():
    headlines = get_headlines(limit=20)
    results_df = analyze_headlines(headlines)
    print(results_df[["text", "compound", "label"]])
    plot_sentiment_distribution(results_df)

if __name__ == "__main__":
    main()