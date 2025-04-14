import os
import finnhub
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("FINNHUB_API_KEY")
client = finnhub.Client(api_key=api_key)

def get_stock_data(ticker):
    try:
        quote = client.quote(ticker)
        rating = client.recommendation_trends(ticker)
        profile = client.company_profile2(symbol=ticker)
        return {
            "quote": quote,
            "recommendation": rating,
            "profile": profile
        }
    except Exception as e:
        return {"error": str(e)}