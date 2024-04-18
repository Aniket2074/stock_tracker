import streamlit as st
import pandas as pd
import requests


# Display logo in the sidebar
st.image("logo-png.png", width=200)



# Create a select box for choosing a stock symbol
selected_stock = st.selectbox(
    "Select a Stock Symbol",
    ("GOOG", "AAPL", "MSFT")
)

# Define an Alpha Vantage API key
API_KEY = 'ULLW8NN5J5GYC3XN'  # Replace with your API key

# Create a "Submit" button
if st.button("Submit"):
    # Fetch stock data based on the selected stock symbol
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={selected_stock}&apikey={API_KEY}'
    response = requests.get(url)
    data = response.json()
    
    # Display the retrieved stock data (example)
    if 'Time Series (Daily)' in data:
        st.write('Stock Price Data for', selected_stock)
        stock_data = data['Time Series (Daily)']
        df = pd.DataFrame(stock_data).T
        st.write(df)



