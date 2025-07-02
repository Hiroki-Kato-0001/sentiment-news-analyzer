import matplotlib.pyplot as plt

def plot_sentiment_distribution(df):
    order = ["positive", "neutral", "negative"]
    df["label"].value_counts().reindex(order).plot(kind="bar", color=["green", "gray", "red"])
    plt.title("Sentiment Distribution of News Headlines")
    plt.xlabel("Sentiment")
    plt.ylabel("Count")
    plt.tight_layout()
    plt.show()