import geodatasets
import pandas as pd
import geopandas
import geodatasets
import contextily as cx

import api_test

nyc_df = geopandas.read_file(geodatasets.get_path("nybb"))
ax = nyc_df.plot(figsize=(10, 10), alpha=0.5, edgecolor="k")


nyc_df.plot()