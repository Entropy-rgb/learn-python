from translate import Translator

translator = Translator(to_lang='es')  # Spanish
# Text to be translated
text = '''My name is Somesh'''
# Perform the translation
translation = translator.translate(text)

# Print the translated text
print('Translated Text:', translation)

