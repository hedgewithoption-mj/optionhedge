import streamlit as st
import pandas as pd
import numpy as np
import yfinance as yf
import plotly.graph_objects as go

# Page configuration
st.set_page_config(
    page_title="OptionHedge - Trading Terminal",
    page_icon="📈",
    layout="wide"
)

st.title("📈 OptionHedge - Multi-Stock Technical & Options Terminal")
st.markdown("Welcome Mulraj! Aapka live trading aur options scanning dashboard yahan run ho raha hai.")

# Sidebar controls
st.sidebar.header("Terminal Controls")
ticker_symbol = st.sidebar.text_input("Enter Stock Ticker (e.g., RELIANCE.NS, TCS.NS, NIFTY)", "RELIANCE.NS")
period = st.sidebar.selectbox("Select Timeframe", ["1mo", "3mo", "6mo", "1y"], index=2)

@st.cache_data
def load_data(ticker, time_period):
    df = yf.download(ticker, period=time_period)
    return df

try:
    with st.spinner(f"Fetching market data for {ticker_symbol}..."):
        data = load_data(ticker_symbol, period)

    if not data.empty:
        st.subheader(f"📊 Price Chart & Indicators for {ticker_symbol}")
        
        # Plotly Candlestick Chart
        fig = go.Figure(data=[go.Candlestick(
            x=data.index,
            open=data['Open'],
            high=data['High'],
            low=data['Low'],
            close=data['Close'],
            name='Candlestick'
        )])
        
        fig.update_layout(
            title=f"{ticker_symbol} Daily Price Movement",
            xaxis_title="Date",
            yaxis_title="Price (INR)",
            template="plotly_dark",
            height=500
        )
        
        st.plotly_chart(fig, use_container_width=True)
        
        # Summary metrics
        st.subheader("Market Summary Metrics")
        latest_close = float(data['Close'].iloc[-1].item())
        prev_close = float(data['Close'].iloc[-2].item())
        price_change = latest_close - prev_close
        pct_change = (price_change / prev_close) * 100
        
        col1, col2, col3 = st.columns(3)
        col1.metric("Latest Close", f"₹{latest_close:.2f}", f"{pct_change:.2f}%")
        col2.metric("Period High", f"₹{float(data['High'].max().item()):.2f}")
        col3.metric("Period Low", f"₹{float(data['Low'].min().item()):.2f}")
        
    else:
        st.error("Data nahi mila. Kripya sahi ticker symbol check karein (jaise RELIANCE.NS).")

except Exception as e:
    st.error(f"Market data fetch karne mein error aayi hai: {e}")
