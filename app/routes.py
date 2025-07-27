from flask import Blueprint, render_template, request
import requests

main = Blueprint('main', __name__)

@main.route("/")
def home():
    return render_template("index.html")

@main.route("/country", methods=["POST"])
def country_info():
    country_name = request.form.get("country", "").strip()

    if not country_name:
        return render_template("result.html", error="Country name cannot be empty.")
    
    try:
        response = requests.get(f"https://restcountries.com/v3.1/name/{country_name}")
        data = response.json()

        if isinstance(data, list):
            country = data[0]
            return render_template("result.html",
                country=country.get("name", {}).get("common", "N/A"),
                capital=country.get("capital", ["N/A"])[0],
                currency=list(country.get("currencies", {}).keys())[0],
                language=list(country.get("languages", {}).values())[0],
                population=country.get("population", "N/A"),
                area=country.get("area", "N/A"),
                flag=country.get("flags", {}).get("png", ""),
                error=None
            )
        else:
            raise ValueError("Country not found")
    except Exception:
        return render_template("result.html", error=f"❌ Error: Could not find \"{country_name}\". Please make sure the country name is spelled correctly.")
