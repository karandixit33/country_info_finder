import requests

def get_country_details(country_name):
    url = f"https://restcountries.com/v3.1/name/{country_name}?fullText=true"

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise error for bad status
        data = response.json()[0]

        country = data.get('name', {}).get('common', 'N/A')
        capital = data.get('capital', ['N/A'])[0]
        currency_code = list(data.get('currencies', {}).keys())[0]
        currency_name = data['currencies'][currency_code]['name']
        languages = ', '.join(data.get('languages', {}).values())

        print("\n--- Country Information ---")
        print(f"Country   : {country}")
        print(f"Capital   : {capital}")
        print(f"Currency  : {currency_name} ({currency_code})")
        print(f"Languages : {languages}\n")

    except Exception as e:
        print("\n❌ Error: Could not fetch data. Please check the country name.\n")

if __name__ == "__main__":
    print("Country Info Finder")
    country_input = input("Enter a country name: ").strip()
    get_country_details(country_input)
