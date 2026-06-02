import requests
import pandas as pd

scheme_codes = [
    125497,  # HDFC Top 100
    119551,  # SBI Bluechip
    120503,  # ICICI Bluechip
    118632,  # Nippon Large Cap
    119092,  # Axis Bluechip
    120841   # Kotak Bluechip
]

for code in scheme_codes:
    url = f"https://api.mfapi.in/mf/{code}"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        df = pd.DataFrame(data["data"])

        df.to_csv(
            f"data/raw/{code}_nav.csv",
            index=False
        )

        print(f"Saved NAV data for {code}")