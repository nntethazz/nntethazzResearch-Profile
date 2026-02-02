# -*- coding: utf-8 -*-
"""
Created on Tue Jan 27 17:32:56 2026

@author: BBarsch
"""

import streamlit as st

st.write("Hello, while you wait -Enjoy the Game!")

st.title("Title heading")

st.write("Hello, Streamlit!")

st.header("On the slide below, pick a number between 1 and 100")

number = st.slider("Pick a number", 1, 100)
st.write(f"You picked: {number}")