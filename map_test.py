import geodatasets
import pandas as pd
import geopandas
import numpy as np
import geodatasets
import contextily as cx
from cartopy import crs as ccrs
from cartopy import feature as cfeature
import matplotlib.pyplot as plt
import geoplot
from geodatasets import get_path

import api_test


main_frame = api_test.operational
final_df = main_frame.rename(columns={'facility_name': 'Location', 'hours_of_operation': 'Hours', 'open': 'Open'})

br_map = geopandas.GeoDataFrame(
    final_df, geometry=geopandas.points_from_xy(final_df["longitude"], final_df["latitude"], crs=4326)
)

m = br_map.explore(tooltip=["Location", "Hours", "Open"])
output_path = r'pch_final\base_map.html'
m.save(output_path)