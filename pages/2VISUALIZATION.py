import streamlit as st
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
import plotly.graph_objs as go
from datetime import datetime, timedelta

st.set_page_config(
        page_icon="chart_with_upwards_trend",
        layout="wide",
    )

# Display logo in the sidebar
st.image("logo-png.png", width=200)


st.title("Stock Data")
    
# Create a sidebar for user input
st.sidebar.header("User Input")
#stock_symbol = st.sidebar.text_input("Enter Stock Symbol (e.g., AAPL)", "MSFT")

# Select box for choosing a stock symbol
stock_symbol = st.sidebar.selectbox(
    "Select a Stock Symbol",
    ("Select a Stock Symbol","GOOG", "AAPL", "MSFT", "MCD", "TSLA","TATAMOTORS.NS", 
     "TATASTEEL.NS", "TATAPOWER.NS", "TCS.NS","NVDA", "AMD", "INTC", "AMZN"))
    
# Fetch stock data using Yahoo Finance
@st.cache_data  # Caching to avoid redundant requests
def get_stock_data(symbol, start_date, end_date):
        stock_data = yf.Ticker(symbol)
        history = stock_data.history(  start=start_date, end=end_date)
        return history
    
# period = st.selectbox('Select Period', ["1d", "5d", "1mo", "3mo", "6mo", "1y", "2y", "5y", "10y", "ytd", "max"])

# Date range selector
today = datetime.today().date()
start_date = st.date_input('Start Date', today - timedelta(days=365))
end_date = st.date_input('End Date', today)

stock_history = get_stock_data(stock_symbol, start_date, end_date)


    
# Display the stock data
st.subheader(f"Stock Data for {stock_symbol}")
st.dataframe(stock_history)


# Add vertical space using CSS margin
st.markdown('<style>div.stSpacer { margin-top: 75px; }</style>', unsafe_allow_html=True)
st.markdown('<div class="stSpacer"></div>', unsafe_allow_html=True)




# Create a candlestick chart
fig = go.Figure(data=[go.Candlestick(
    x=stock_history.index,
    open=stock_history["Open"],
    high=stock_history["High"],
    low=stock_history["Low"],
    close=stock_history["Close"]
)])
st.subheader(f"Candlestick Chart for {stock_symbol}")
fig.update_layout(
    #title=f"{stock_symbol} Candlestick Chart",
    xaxis_title="Date",
    yaxis_title="Price",
)

st.plotly_chart(fig)



# Add vertical space using CSS margin
st.markdown('<style>div.stSpacer { margin-top: 75px; }</style>', unsafe_allow_html=True)
st.markdown('<div class="stSpacer"></div>', unsafe_allow_html=True)



    
# Plot the time series graph
st.subheader(f"Time Series Graph for {stock_symbol}")
plt.figure(figsize=(10, 5))
plt.title(f"{stock_symbol} Stock Price Over Time")
plt.plot(stock_history.index, stock_history["Close"])
plt.xlabel("Date")
plt.ylabel("Closing Price")
st.pyplot(plt)
    
# st.sidebar.write("Data Source: Yahoo Finance")



# Add vertical space using CSS margin
st.markdown('<style>div.stSpacer { margin-top: 75px; }</style>', unsafe_allow_html=True)
st.markdown('<div class="stSpacer"></div>', unsafe_allow_html=True)




# Volume Chart
st.subheader(f"Volume Chart for {stock_symbol}")
plt.figure(figsize=(10, 5))
plt.bar(stock_history.index, stock_history['Volume'], color='blue')
plt.title("Volume of Trading")
plt.xlabel("Date")
plt.ylabel("Volume")
st.pyplot(plt)



# Add vertical space using CSS margin
st.markdown('<style>div.stSpacer { margin-top: 75px; }</style>', unsafe_allow_html=True)
st.markdown('<div class="stSpacer"></div>', unsafe_allow_html=True)



# Histogram of Daily Returns
st.subheader(f"Histogram of Daily Returns for {stock_symbol}")
returns = stock_history['Close'].pct_change().dropna()
plt.figure(figsize=(10, 5))
plt.hist(returns, bins=20, edgecolor='black')
plt.title("Histogram of Daily Returns")
plt.xlabel("Daily Returns")
plt.ylabel("Frequency")
st.pyplot(plt)


