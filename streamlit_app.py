import streamlit as st
import pickle

vectorization = pickle.load(open("vectorization.pkl", "rb"))
model = pickle.load(open("LR_model.pkl", "rb"))

st.title("Fake News Detection System")

input_text = st.text_area("Enter News Text")

if st.button("Predict"):
    vector_input = vectorization.transform([input_text])
    prediction = model.predict(vector_input)

    if prediction[0] == 1:
        st.error("Fake News ")
    else:
        st.success("Real News ")