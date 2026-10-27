import streamlit as st

# 1. Page Configuration (Wide layout for trading terminal look)
st.set_page_config(
    page_title="OptionHedge Terminal",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Custom CSS for styling the header, tabs, and dark terminal aesthetic
st.markdown("""
    <style>
        /* Main background & styling */
        .main {
            background-color: #0e1117;
        }
        /* Top Header Container */
        .top-header {
            display: flex;
            align-items: center;
            justify-content: space-between;
            background-color: #161b22;
            padding: 10px 20px;
            border-radius: 8px;
            margin-bottom: 20px;
            border: 1px solid #30363d;
        }
        .logo-title {
            font-size: 22px;
            font-weight: bold;
            color: #58a6ff;
        }
        .index-ticker {
            display: flex;
            gap: 30px;
            font-size: 14px;
            color: #c9d1d9;
        }
        .ticker-item {
            background: #21262d;
            padding: 5px 12px;
            border-radius: 6px;
            border: 1px solid #30363d;
        }
    </style>
""", unsafe_allow_html=True)

# 3. Top Header: Logo (Top Left) & Indices with price and movement
st.markdown("""
    <div class="top-header">
        <div class="logo-title">⚡ OptionHedge</div>
        <div class="index-ticker">
            <div class="ticker-item"><b>NIFTY 50:</b> 22,600.00 <span style="color: #2ea043;">+120.50 (+0.54%)</span></div>
            <div class="ticker-item"><b>SENSEX:</b> 74,120.80 <span style="color: #2ea043;">+340.20 (+0.46%)</span></div>
            <div class="ticker-item"><b>BANKNIFTY:</b> 48,150.30 <span style="color: #da3633;">-45.10 (-0.09%)</span></div>
        </div>
    </div>
""", unsafe_allow_html=True)

# 4. Layout Structure: 3 Columns (Left Sidebar Tabs | Center Chart | Right Watchlist)
left_nav, center_chart, right_sidebar = st.columns([1.2, 4.5, 2.3])

with left_nav:
    st.markdown("### 🧭 Navigation")
    # Left side tabs / radio options
    selected_tab = st.radio(
        "Menu",
        ["🏠 Home", "⚡ Scalper", "📊 Strategy", "🔍 Scanner"],
        label_visibility="collapsed"
    )
    
    st.markdown("---")
    st.markdown("### ⚙️ Quick Filters")
    st.selectbox("Segment", ["Futures & Options", "Equities"])
    st.selectbox("Timeframe", ["1m", "5m", "15m", "1H", "1D"])

with center_chart:
    st.markdown("### 📊 TradingView Chart View")
    
    # Placeholder for TradingView chart integration or Plotly chart
    # (Aap yahan apna Plotly candlestick chart code render kar sakte hain)
    st.info("💡 TradingView Chart Component / Plotly Candlestick Render Area")
    
    # Dummy container to simulate chart height
    chart_container = st.container(height=400)
    with chart_container:
        st.write("Chart data stream active for selected instrument...")
        # st.plotly_chart(fig, use_container_width=True)

    # Bottom metrics or technical indicator panel below chart
    ind_col1, ind_col2, ind_col3 = st.columns(3)
    with ind_col1:
        st.metric("RSI (14)", "58.4", "Bullish")
    with ind_col2:
        st.metric("MACD Signal", "Bullish Crossover", "+12.4")
    with ind_col3:
        st.metric("PCR Ratio", "1.15", "Positive")

with right_sidebar:
    st.markdown("### 📋 Watchlist")
    watchlist_tab = st.tabs(["No. 1", "No. 2", "No. 3"])
    
    with watchlist_tab[0]:
        st.text_input("🔍 Search symbol...", placeholder="e.g. RELIANCE, TCS")
        
        # Sample Watchlist Items mimicking the video layout
        watchlist_data = [
            ("RELIANCE", "₹2,840.50", "+1.2%"),
            ("TCS", "₹3,910.00", "-0.4%"),
            ("INFY", "₹1,650.20", "+0.8%"),
            ("NIFTY 50", "₹22,600.00", "+0.54%"),
            ("SENSEX", "₹74,120.80", "+0.46%")
        ]
        
        for symbol, price, change in watchlist_data:
            col_a, col_b = st.columns([2, 1])
            with col_a:
                st.markdown(f"**{symbol}**<br><span style='font-size:12px; color:gray;'>{price}</span>", unsafe_allow_html=True)
            with col_b:
                color = "green" if "+" in change else "red"
                st.markdown(f"<span style='color:{color}; font-size:13px;'>{change}</span>", unsafe_allow_html=True)
            st.divider()

    with watchlist_tab[1]:
        st.write("Watchlist 2 items...")

    with watchlist_tab[2]:
        st.write("Watchlist 3 items...")

    st.markdown("### ⚡ Live Scanners")
    st.selectbox("Scanner Preset", ["Top Gainers", "Top Losers", "Opening Range Breakout"])
    st.write("• *AOLPORECH* — ₹770.08 (+4.1%)")
    st.write("• *ETERNA* — ₹1,718.55 (+3.2%)")
