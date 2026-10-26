import streamlit as st

st.title("📈 OptionHedge - Trading Terminal")
st.write("Welcome Mulraj! Aapka trading terminal successfully live ho gaya hai.")

# Ek chota sa test input
stock = st.text_input("Enter Stock Symbol:", "RELIANCE")
st.write(f"Currently viewing setup for: **{stock}**")

if st.button("Run Scan"):
    st.success(f"Market scan active for {stock}. All systems normal!")
