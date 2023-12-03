import streamlit as st
import plotly.express as px

from analyzer import analyze

st.title("Diary Tone")
st.subheader("Positivity")

# Pulling from analyzer.py the values from NLTK Sentiment Analyzer
data = analyze()

# Pull out the dates
dates = list(data.keys())

# pull out the positive values via list comprehension
pos_value = [dict["pos"] for dict in data.values()]
neg_value = [dict["neg"] for dict in data.values()]

# Place values into the graphs
pos_figure = px.line(x=dates, y=pos_value, labels={"x": "Date", "y": "Positive Values"})
st.plotly_chart(pos_figure)

st.subheader("Negativity")

neg_figure = px.line(x=dates, y=neg_value, labels={"x": "Date", "y": "Negative Values"})
st.plotly_chart(neg_figure)