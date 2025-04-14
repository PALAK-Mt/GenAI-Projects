from app.tools.finnhub_tool import get_stock_data
from app.tools.news_search_tool import get_latest_news
from transformers import pipeline

summarizer = pipeline("summarization", model="google/pegasus-xsum")

def analyze_stock(ticker):
    # Agent 1: Get stock data
    stock_data = get_stock_data(ticker)

    # Agent 2: Get financial news
    news_articles = get_latest_news(ticker)

    # Agent 3 (optional): Summarize each article
    for article in news_articles:
        summary_text = article.get("summary", "")
        if summary_text and summary_text != "Summary could not be extracted.":
            try:
                summary = summarizer(summary_text, max_length=60, min_length=20, do_sample=False)
                article["summary"] = summary[0]["summary_text"]
            except Exception:
                continue

    return {
        "stock_data": stock_data,
        "news": news_articles
    }