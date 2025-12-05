import pandas as pd
from sodapy import Socrata
from IPython.display import display

client = Socrata("data.cityofnewyork.us", None)

results = client.get("i7jb-7jku", limit=2000)

#convert to pandas dataframe
results_df = pd.DataFrame.from_records(results)

operational = results_df[results_df["status"] == "Operational"]
operational.to_csv('bathrooms.csv', index=False)