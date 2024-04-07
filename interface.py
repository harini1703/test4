import pickle
import streamlit as st
from datetime import date
import numpy as np
import pandas as pd
import joblib


# Load the model
pickle_in = open('fbpro.pkl', 'rb')
clf = pickle.load(pickle_in)

st.header("Streamlined Wind Speed Forecasting: A Web-Based Machine Learning Approach for Wind Mill Operators with Real-Time Data Using Streamlit")
