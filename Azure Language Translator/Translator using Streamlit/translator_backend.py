import requests

def translate_text(api_key, endpoint, region, text, from_lang, to_lang):
    path = '/translate'
    constructed_url = f"{endpoint}{path}"
    headers = {
        'Ocp-Apim-Subscription-Key': api_key,
        'Ocp-Apim-Subscription-Region': region,
        'Content-Type': 'application/json',
    }
    params = {
        'api-version': '3.0',
        'from': from_lang,
        'to': to_lang,
    }
    body = [{'text': text}]
    response = requests.post(constructed_url, params=params, headers=headers, json=body)
    response.raise_for_status()
    return response.json()
