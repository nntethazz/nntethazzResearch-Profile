# -*- coding: utf-8 -*-
"""
Created on Tue Jan 27 17:38:34 2026

@author: BBarsch
1st one to be edited
"""
import streamlit as st
import subprocess

file = "app.py"
file = "app_plots.py"
file = "app_profiler.py"
file = "app_profiler_menus.py"

#pressed = st.button("Press Me")
#print(pressed)
subprocess.Popen(
    ["streamlit", "run", file], shell=True

)
