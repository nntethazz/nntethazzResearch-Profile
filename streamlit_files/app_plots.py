# My Plot of data

import pandas as pd
import plotly.express as px
import streamlit as st

st.title("Research Profile for Njabulo S. Ntetha")

st.write("Welcome to my Profile Page - showcasing my previous studies")

st.header("Sample Data")

data = pd.DataFrame({"x": [1, 2, 3], "y": [10, 20, 30]})

# Display the data in the Streamlit app
st.write(data)
st.write("________________________________")
st.dataframe(data)

# Create a Plotly figure
fig = px.line(data, x="x", y="y", title="Simple Plotly Example")

# Display the plot in the Streamlit app
st.plotly_chart(fig)