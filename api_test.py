import pandas as pd
from sodapy import Socrata
from IPython.display import display

client = Socrata("data.cityofnewyork.us", None)

results = client.get("i7jb-7jku", limit=2000)

#convert to pandas dataframe
results_df = pd.DataFrame.from_records(results)
operational = results_df[results_df["status"] == "Operational"]

columns_to_drop = ["location_type", "status", "changing_stations", "latitude", "longitude", "location_1", ":@computed_region_yeji_bk3q", ":@computed_region_sbqj_enih", ":@computed_region_92fq_4b7q", ":@computed_region_f5dn_yrer", "restroom_type", "open", "hours_of_operation", "website", "additional_notes"]
final_df = results_df.drop(columns=columns_to_drop)
final_df["accessibility"] = final_df["accessibility"].fillna("Not accessible")
print(final_df)
#bathrooms_csv = operational.to_csv('bathrooms.csv', index=False)