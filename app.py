import streamlit as st


st.write("App is working!")

import streamlit as st
import pickle
import numpy as np

st.title("EduPredict – Student Performance Predictor")

# Input field
hours = st.number_input("Enter study hours:", min_value=0.0, max_value=24.0, step=0.5)

if st.button("Predict"):
    
    # Model load karo
    model = pickle.load(open("model.pkl", "rb"))
    
    prediction = model.predict([[hours]])
    
    st.success(f"Predicted Score: {prediction[0]:.2f}")
