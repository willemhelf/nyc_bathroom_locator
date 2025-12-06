import pandas as pd
from sodapy import Socrata
from IPython.display import display

client = Socrata("data.cityofnewyork.us", None)

results = client.get("i7jb-7jku", limit=2000)

#convert to pandas dataframe and filter out non-operational locations
results_df = pd.DataFrame.from_records(results)
operational = results_df[results_df["status"] == "Operational"]

#remove unnecessary columns, replace "NaN" entries with text, and rename remaining columns
def clean_df(df):
    columns_to_drop = ["location_type", "operator", "status", "changing_stations", "latitude", "longitude", "location_1", ":@computed_region_yeji_bk3q", ":@computed_region_sbqj_enih", ":@computed_region_92fq_4b7q", ":@computed_region_f5dn_yrer", "restroom_type", "website", "additional_notes"]
    df = results_df.drop(columns=columns_to_drop)
    df["accessibility"] = df["accessibility"].fillna("No")
    df["hours_of_operation"] = df["hours_of_operation"].fillna("-")
    df["open"] = df["open"].fillna("-")
    df.rename(columns={'facility_name': 'Location',  "accessibility": 'Accessible?',  'open': 'Open', 'hours_of_operation': 'Hours'}, inplace=True)
    return df

final_df = clean_df(operational)
final_list = final_df.values.tolist()
print(final_list)

#bathrooms_csv = operational.to_csv('bathrooms.csv', index=False)