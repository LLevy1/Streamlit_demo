"""
This would be the 'traditional' way to the test the app.

import streamlit as st
from textblob import TextBlob

# Set up the app
st.title("Spelling correction with TextBlob")
st.write("Enter some text, and the model will check your spelling.")

# Simulate user input
user_input = "I havv goood speling"
st.text_area("Enter text for spell checker:", value=user_input)

# Create a TextBlob object and analyze sentiment
blob = TextBlob(user_input)

Check the corrected spelling
corrected_text = str(blob.correct())
self.assertEqual(corrected_text, "I have good spelling")
"""

# insstead all you need is this:

from streamlit.testing.v1 import AppTest


def test_spelling():
    at = AppTest.from_file("app/spell_check.py").run()
    at.text_area[0].input("I havv goood speling").run()
    corrected_text = at.markdown[1].value
    assert corrected_text == "Correct spelling: I have good spelling"


# i've added some more tests to check the title and markdown


def test_app():
    at = AppTest.from_file("app/spell_check.py")
    at.run()
    assert not at.exception


def test_title():
    at = AppTest.from_file("app/spell_check.py")
    at.run()
    assert at.title[0].value == "Spelling correction with TextBlob"


def test_markdown():
    at = AppTest.from_file("app/spell_check.py")
    at.run()
    assert (
        at.markdown[0].value
        == "Enter some text, and the model will check your spelling."
    )
