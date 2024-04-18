import streamlit as st
from newsapi import NewsApiClient

# Display logo in the sidebar
st.image("logo-png.png", width=200)

# Initialize News API client
newsapi = NewsApiClient(api_key='4ab8a466e759412b9fa3a92619e5ef86')

# Function to fetch stock market news
def fetch_stock_news(query):
    try:
        # Fetch news articles
        news_articles = newsapi.get_everything(q=query, language='en', sort_by='relevancy')
        articles = news_articles['articles']
        return articles
    except Exception as e:
        st.error(f"Error fetching news: {e}")
        return []

def main():
    st.title("Stock Market News")

    # Input query
    query = st.text_input("Enter your query (e.g., stock market)","stock market")

    # Fetch and display stock market news
    if query:
        st.info("Fetching stock market news...")
        articles = fetch_stock_news(query)
        if articles:
            for article in articles:
                st.write(f"- **{article['title']}**")
                st.write(f"  {article['description']}")
                st.write(f"  Source: {article['source']['name']}")
                st.write(f"  Published at: {article['publishedAt']}")
                st.write(f"  [Read more]({article['url']})")
        else:
            st.warning("No news available")

if __name__ == "__main__":
    main()
