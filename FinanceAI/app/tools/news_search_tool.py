from duckduckgo_search import DDGS
from newspaper import Article

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
                    results.append({
                        "title": article.title or "No Title",
                        "url": url,
                        "summary": article.text[:500] or "No summary available."
                    })
                except Exception:
                    results.append({
                        "title": result.get("title") or "Untitled",
                        "url": url,
                        "summary": "Summary could not be extracted."
                    })

    except Exception as e:
        return [{"error": f"News fetch failed: {str(e)}"}]

    return results