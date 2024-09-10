import streamlit as st
from translator_backend import translate_text

# Azure Translator API credentials
API_KEY = 'AZURE_TRANSLATOR_KEY'
ENDPOINT = 'https://api.cognitive.microsofttranslator.com/'  # AZURE_TRANSLATOR_ENDPOINT
REGION = 'AZURE_TRANSLATOR_REGION'

# Mapping of language names to their codes
LANGUAGE_CODES = {
    "😊👉🏻--Select Language--👈🏻😊" : "-",
    "Afrikaans": "af",
    "Albanian": "sq",
    "Amharic": "am",
    "Arabic": "ar",
    "Armenian": "hy",
    "Assamese": "as",
    "Azerbaijani (Latin)": "az",
    "Bangla": "bn",
    "Bashkir": "ba",
    "Basque": "eu",
    "Bhojpuri": "bho",
    "Bodo": "brx",
    "Bosnian (Latin)": "bs",
    "Bulgarian": "bg",
    "Cantonese (Traditional)": "yue",
    "Catalan": "ca",
    "Chinese (Literary)": "lzh",
    "Chinese Simplified": "zh-Hans",
    "Chinese Traditional": "zh-Hant",
    "chiShona": "sn",
    "Croatian": "hr",
    "Czech": "cs",
    "Danish": "da",
    "Dari": "prs",
    "Divehi": "dv",
    "Dogri": "doi",
    "Dutch": "nl",
    "English": "en",
    "Estonian": "et",
    "Faroese": "fo",
    "Fijian": "fj",
    "Filipino": "fil",
    "Finnish": "fi",
    "French": "fr",
    "French (Canada)": "fr-ca",
    "Galician": "gl",
    "Georgian": "ka",
    "German": "de",
    "Greek": "el",
    "Gujarati": "gu",
    "Haitian Creole": "ht",
    "Hausa": "ha",
    "Hebrew": "he",
    "Hindi": "hi",
    "Hmong Daw (Latin)": "mww",
    "Hungarian": "hu",
    "Icelandic": "is",
    "Igbo": "ig",
    "Indonesian": "id",
    "Inuinnaqtun": "ikt",
    "Inuktitut": "iu",
    "Inuktitut (Latin)": "iu-Latn",
    "Irish": "ga",
    "Italian": "it",
    "Japanese": "ja",
    "Kannada": "kn",
    "Kashmiri": "ks",
    "Kazakh": "kk",
    "Khmer": "km",
    "Kinyarwanda": "rw",
    "Klingon": "tlh-Latn",
    "Klingon (plqaD)": "tlh-Piqd",
    "Konkani": "gom",
    "Korean": "ko",
    "Kurdish (Central)": "ku",
    "Kurdish (Northern)": "kmr",
    "Kyrgyz (Cyrillic)": "ky",
    "Lao": "lo",
    "Latvian": "lv",
    "Lithuanian": "lt",
    "Lingala": "ln",
    "Lower Sorbian": "dsb",
    "Luganda": "lug",
    "Macedonian": "mk",
    "Maithili": "mai",
    "Malagasy": "mg",
    "Malay (Latin)": "ms",
    "Malayalam": "ml",
    "Maltese": "mt",
    "Maori": "mi",
    "Marathi": "mr",
    "Mongolian (Cyrillic)": "mn-Cyrl",
    "Mongolian (Traditional)": "mn-Mong",
    "Myanmar": "my",
    "Nepali": "ne",
    "Norwegian": "nb",
    "Nyanja": "nya",
    "Odia": "or",
    "Pashto": "ps",
    "Persian": "fa",
    "Polish": "pl",
    "Portuguese (Brazil)": "pt",
    "Portuguese (Portugal)": "pt-pt",
    "Punjabi": "pa",
    "Queretaro Otomi": "otq",
    "Romanian": "ro",
    "Rundi": "run",
    "Russian": "ru",
    "Samoan (Latin)": "sm",
    "Serbian (Cyrillic)": "sr-Cyrl",
    "Serbian (Latin)": "sr-Latn",
    "Sesotho": "st",
    "Sesotho sa Leboa": "nso",
    "Setswana": "tn",
    "Sindhi": "sd",
    "Sinhala": "si",
    "Slovak": "sk",
    "Slovenian": "sl",
    "Somali (Arabic)": "so",
    "Spanish": "es",
    "Swahili (Latin)": "sw",
    "Swedish": "sv",
    "Tahitian": "ty",
    "Tamil": "ta",
    "Tatar (Latin)": "tt",
    "Telugu": "te",
    "Thai": "th",
    "Tibetan": "bo",
    "Tigrinya": "ti",
    "Tongan": "to",
    "Turkish": "tr",
    "Turkmen (Latin)": "tk",
    "Ukrainian": "uk",
    "Upper Sorbian": "hsb",
    "Urdu": "ur",
    "Uyghur (Arabic)": "ug",
    "Uzbek (Latin)": "uz",
    "Vietnamese": "vi",
    "Welsh": "cy",
    "Xhosa": "xh",
    "Yoruba": "yo",
    "Yucatec Maya": "yua",
    "Zulu": "zu",
}

def main():
    st.title("Azure Language Translator")

    # Language names for dropdown
    language_names = list(LANGUAGE_CODES.keys())
    from_language_name = st.selectbox("Select the source language:", language_names)
    to_language_name = st.selectbox("Select the target language:", language_names)

    # User input
    text_to_translate = st.text_area("Enter text to translate:")

    # Convert language names to codes
    from_language_code = LANGUAGE_CODES[from_language_name]
    to_language_code = LANGUAGE_CODES[to_language_name]

    if st.button("Translate"):
        if not text_to_translate:
            st.error("Please enter some text to translate.")
        else:
            try:
                translation_result = translate_text(API_KEY, ENDPOINT, REGION, text_to_translate, from_language_code, to_language_code)
                translated_text = translation_result[0]['translations'][0]['text']
                st.subheader("Translated Text:")
                st.write(translated_text)
            except Exception as e:
                st.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
