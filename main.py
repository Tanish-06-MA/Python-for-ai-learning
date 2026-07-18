import requests
import pandas as pd

url="https://catfact.ninja/fact"


response = requests.get(url)
data =response.json()



df = pd.DataFrame({
    'm': [data["fact"]]
})

print(df)