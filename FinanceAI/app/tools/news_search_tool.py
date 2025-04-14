from transformers import pipeline
from newspaper import Article
from duckduckgo_search import DDGS

# Initialize the sentiment analysis pipeline from Hugging Face
sentiment_analyzer = pipeline("sentiment-analysis")

def get_latest_news(ticker):
    results = []
    try:
        with DDGS() as ddgs:
            search_results = ddgs.text(f"{ticker} stock news", max_results=5)
            for result in search_results:
                url = result.get("href") or result.get("url")
                if not url:
                    continue

                try:
                    article = Article(url)
                    article.download()
                    article.parse()
                    
                    # Perform sentiment analysis on the article content
                    sentiment = sentiment_analyzer(article.text[:512])  # Limit text for analysis

                    # Append sentiment result to news article data
                    results.append({
                        "title": article.title or "No Title",
                        "url": url,
                        "summary": article.text[:500] or "No summary available.",
                        "sentiment": sentiment[0]["label"],  # Sentiment: POSITIVE/NEGATIVE/NEUTRAL
                        "confidence": sentiment[0]["score"]  # Sentiment score
                    })
                except Exception as e:
                    results.append({
                        "title": result.get("title") or "Untitled",
                        "url": url,
                        "summary": "Summary could not be extracted.",
                        "sentiment": "N/A",
                        "confidence": "N/A"
                    })

    except Exception as e:
        return [{"error": f"News fetch failed: {str(e)}"}]

    return results
