import streamlit as st
import pandas as pd
import numpy as np
import yfinance as yf
from sklearn.model_selection import train_test_split
from statsmodels.tsa.arima.model import ARIMA
import plotly.graph_objs as go

# Display logo in the sidebar
st.image("logo-png.png", width=200)

st.title('Stock Price Prediction')

# User input for stock symbol, start date, and end date
stock_symbol = st.selectbox('Select Stock Symbol', ["GOOG", "AAPL", "MSFT", "MCD", "TSLA","TATAMOTORS.NS", 
     "TATASTEEL.NS", "TATAPOWER.NS", "TCS.NS","NVDA", "AMD", "INTC", "AMZN"])  # Add more options as needed
start_date = st.date_input('Start Date', value=pd.to_datetime('2020-01-01'))
end_date = st.date_input('End Date', value=pd.to_datetime('2024-01-01'))

# Fetch data using yfinance
stock_data = yf.download(stock_symbol, start=start_date, end=end_date)

# Extract 'Close' prices as sales data
y = stock_data['Close']

# Define ARIMA model
order = (5, 1, 0)  # ARIMA parameters (p, d, q)
model = ARIMA(y, order=order)

# Train the ARIMA model
arima_model = model.fit()

# Make future predictions
forecast_periods = 7  # Number of periods to forecast into the future
future_index = pd.date_range(start=y.index[-1], periods=forecast_periods + 1)[1:]  # Generate future dates

# Forecast future values
y_forecast = arima_model.forecast(steps=forecast_periods)

# Plot actual and forecasted values
fig = go.Figure()

# Add actual values
fig.add_trace(go.Scatter(x=y.index, y=y, mode='lines', name='Actual'))

# Add forecasted values
fig.add_trace(go.Scatter(x=future_index, y=y_forecast, mode='lines', name='Forecast'))

# Update layout
fig.update_layout(title='Actual vs Forecasted Stock Prices', xaxis_title='Date', yaxis_title='Stock Price')

# Display plot
st.plotly_chart(fig)
