from googletrans import Translator

translator = Translator()

def translate_text(text, lang):
    if lang == "ta":
        return text
    try:
        result = translator.translate(text, dest=lang)
        return result.text
    except Exception as e:
        return text