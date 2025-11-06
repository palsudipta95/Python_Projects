import requests
from win11toast import toast  
import json

url = "https://disease.sh/v3/covid-19/all"

try:
    response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
    response.raise_for_status()

    data = response.json()
    cases = data['cases']
    deaths = data['deaths']
    recovered = data['recovered']

    toast(
        "COVID-19 Update",
        f"Total Cases: {cases:,}\nDeaths: {deaths:,}",
        icon='https://cdn-icons-png.flaticon.com/128/2948/2948038.png'
    )

except Exception as e:
    print("Error:", e)