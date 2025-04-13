from app.tools.finnhub_tool import get_stock_data
from app.tools.news_search_tool import get_latest_news
from transformers import pipeline

summarizer = pipeline("summarization", model="google/pegasus-xsum")

def analyze_stock(ticker):
    stock_data = get_stock_data(ticker)
    news = get_latest_news(ticker)

    for article in news:
        if "summary" in article and article["summary"] != "Summary could not be extracted.":
            try:
                article["summary"] = summarizer(article["summary"], max_length=60, min_length=20, do_sample=False)[0]['summary_text']
            except Exception:
                continue

    return {
        "stock_data": stock_data,
        "news": news
    }