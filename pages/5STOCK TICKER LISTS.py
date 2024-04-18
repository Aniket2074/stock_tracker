import streamlit as st

# Display logo in the sidebar
st.image("logo-png.png", width=200)

# Defne header
st.title("Stock Ticker Symbols")

# Define a list
my_list = ["Google (GOOG)", "Apple (AAPL)", "Microsoft (MSFT)", "Tata motors (TATAMOTORS.NS)", 
           "Tata Consultancy services (TCS.NS)", "Tata Steel Ltd (TATASTEEL.NS)","Tesla (TSLA)","Mcdonalds (MCD)", "Tata Power (TATAPOWER.NS)",
           "Intel Corporation (INTC)", "Nvidia (NVDA)", "Advanced Micro Devices (AMD)","Amazon (AMZN)"]

# Display bulleted list using Markdown
st.markdown("\n".join([f"- {item}" for item in my_list]))
