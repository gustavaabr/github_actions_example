import requests
import pandas as pd
from datetime import datetime
import os

url = "https://api.spaceflightnewsapi.net/v4/articles/?limit=10"
response = requests.get(url)

# Tjek 
response.raise_for_status() 
data = response.json()

# Indlæser i Pandas og renser
df = pd.DataFrame(data['results'])

# Rens af data
kolonner_jeg_vil_have = ['id', 'title', 'published_at', 'news_site', 'url']
df = df[kolonner_jeg_vil_have]

# Konverterer 'published_at' til et rigtigt dato-format og fjerner tidszonen
df['published_at'] = pd.to_datetime(df['published_at']).dt.tz_localize(None)

# Sorter efter nyeste artikler
df = df.sort_values(by='published_at', ascending=False)
print(f"Rensede {len(df)} artikler.")

# Gemmer systematisk
os.makedirs('data', exist_ok=True)
dags_dato = datetime.now().strftime("%Y-%m-%d")
filnavn = f"data/nyheder_{dags_dato}.csv"

# Gem til CSV
df.to_csv(filnavn, index=False)
print(f"Data gemt succesfuldt i {filnavn}")