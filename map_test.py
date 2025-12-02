import requests 
import pandas as pd
import geopandas
import numpy as np
import geodatasets
import pyogrio
import contextily as cx
from cartopy import crs as ccrs
from cartopy import feature as cfeature
import matplotlib.pyplot as plt
import geoplot
from geodatasets import get_path
import folium
import api_test

main_frame = api_test.operational
final_df = main_frame.rename(columns={'facility_name': 'Location', 'hours_of_operation': 'Hours', 'open': 'Open'})

br_map = geopandas.GeoDataFrame(
    final_df, geometry=geopandas.points_from_xy(final_df["longitude"], final_df["latitude"], crs=4326)
)

tooltip_map = br_map.explore(tooltip=["Location", "Hours", "Open"])

'''
output_path = r'base_map.html'
m.save(output_path)
'''
json_map = br_map.to_file("./map.geojson", driver="GeoJSON")

filename = "map.geojson"
file = open(filename)
df = geopandas.read_file(file)

m = folium.Map(location=(40.7128, -74.0060), tiles="cartodb positron")

folium.GeoJson(
    br_map,
    name="Subway Stations",
    marker=folium.Circle(radius=4, fill_color="orange", fill_opacity=0.4, color="black", weight=1),
    tooltip=folium.GeoJsonTooltip(fields=["Location", "Hours", "Open"]),
    popup=folium.GeoJsonPopup(fields=["Location", "Hours", "Open"]),
    highlight_function=lambda x: {"fillOpacity": 0.8},
    zoom_on_click=True,
).add_to(m)


#folium.GeoJson(filename).add_to(m)

m 

