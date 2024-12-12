import streamlit as st
from textblob import TextBlob

# Streamlit UI
st.title("Spelling correction with TextBlob")
st.write("Enter some text, and the model will check your spelling.")

# Text input
user_input = st.text_area("Enter text for spell checker:")

# When the user submits text
if user_input:
    # Create a TextBlob object and analyze sentiment
    blob = TextBlob(user_input)
    # Display the results
    st.write(f"Correct spelling: {blob.correct()}")
