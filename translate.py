# translate.py

from deep_translator import GoogleTranslator

def translate_text(text, target_language):
    try:
        # Translate the text
        translated = GoogleTranslator(source='auto', target=target_language).translate(text)
        return translated
    except Exception as e:
        return f"An error occurred: {e}"

if __name__ == "__main__":
    # Example usage
    text_to_translate = input("Enter text to translate: ")
    target_lang = input("Enter target language (e.g., 'fr' for French, 'es' for Spanish): ")
    
    result = translate_text(text_to_translate, target_lang)
    print(f"Translated text: {result}")