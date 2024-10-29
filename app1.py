import streamlit as st
from googletrans import Translator

# Create a Translator object
translator = Translator()

# Set the title of the app
st.title("Simple Translation App")

# Create a text input for the user to enter text
text_to_translate = st.text_area("Enter text to translate:")

# Create a dropdown for selecting the target language
languages = {
    'Spanish': 'es',
    'French': 'fr',
    'German': 'de',
    'Italian': 'it',
    'Chinese (Simplified)': 'zh-cn',
    'Japanese': 'ja',
    'Russian': 'ru',
    'Arabic': 'ar'
}

target_language = st.selectbox("Select target language:", list(languages.keys()))

# Button to perform translation
if st.button("Translate"):
    if text_to_translate:
        # Translate the text
        translated = translator.translate(text_to_translate, dest=languages[target_language])
        # Display the translated text
        st.success(f'Translated text: {translated.text}')
    else:
        st.error("Please enter text to translate.")