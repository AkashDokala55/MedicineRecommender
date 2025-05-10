import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("OPENFDA_API_KEY")

def process_input(input_data):
    symptoms = input_data.lower().strip().split(',')
    return [sym.strip() for sym in symptoms if sym.strip()]

def fetch_medicine_data(symptom):
    base_url = "https://api.fda.gov/drug/label.json"
    params = {
        'search': f'indications_and_usage:{symptom}',
        'limit': 10,
        'api_key': API_KEY
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        data = response.json()

        results = []
        for item in data.get("results", []):
            brand_names = item.get("openfda", {}).get("brand_name", [])
            indications = item.get("indications_and_usage", [])

            # Skip if no brand name or indications
            if not brand_names or not indications:
                continue

            medicine = {
                'name': brand_names[0],
                'description': indications[0],
                'price': "30.00"  # Fixed price as a string for safe rendering
            }
            results.append(medicine)

        return results

    except Exception as e:
        print("Error fetching medicine data:", e)
        return []
