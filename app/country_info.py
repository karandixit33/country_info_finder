# app/country_info.py

import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_BASE_URL = os.getenv("API_BASE_URL", "https://restcountries.com/v3.1/name")
FULLTEXT_QUERY = os.getenv("FULLTEXT_QUERY", "true")

def get_country_details(country_name):
    url = f"{API_BASE_URL}/{country_name}?fullText={FULLTEXT_QUERY}"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()[0]

        country = data.get('name', {}).get('common', 'N/A')
        capital = data.get('capital', ['N/A'])[0]
        currency_code = list(data.get('currencies', {}).keys())[0]
        currency_name = data['currencies'][currency_code]['name']
        languages = ', '.join(data.get('languages', {}).values())
        population = data.get('population', 'N/A')
        area = data.get('area', 'N/A')
        flag_url = data.get('flags', {}).get('png', '')

        return {
            'country': country,
            'capital': capital,
            'currency': f"{currency_name} ({currency_code})",
            'languages': languages,
            'population': f"{population:,}",
            'area': f"{area:,} km²",
            'flag_url': flag_url
        }

    except Exception:
        return None
