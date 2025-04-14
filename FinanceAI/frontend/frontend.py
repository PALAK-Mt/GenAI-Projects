import streamlit as st
import requests

st.title("📊 Financial AI Agent")

ticker = st.text_input("Enter Stock Ticker (e.g., AAPL)", value="AAPL")

if st.button("Analyze"):
    with st.spinner("Analyzing with multi-agent system..."):
        try:
            response = requests.get(f"http://127.0.0.1:8001/analyze?ticker={ticker}")
            data = response.json()

            st.subheader("Stock Data")
            st.json(data.get("stock_data", {}))

            st.subheader("Financial News")
            for article in data.get("news", []):
                st.markdown(f"**{article.get('title')}**")
                st.markdown(f"{article.get('summary')}")
                st.markdown(f"[Read more]({article.get('url')})")
                st.markdown("---")

        except Exception as e:
            st.error(f"Error: {e}")
