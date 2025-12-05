import geopandas
import folium
import api_test
import io
from folium.plugins import Draw, MousePosition, HeatMap
from PySide6 import QtWidgets, QtWebEngineWidgets, QtCore


main_frame = api_test.operational
final_df = main_frame.rename(columns={'facility_name': 'Location', 'hours_of_operation': 'Hours', 'open': 'Open'})

br_map = geopandas.GeoDataFrame(
    final_df, geometry=geopandas.points_from_xy(final_df["longitude"], final_df["latitude"], crs=4326)
)

geo_map = folium.Map(location=(40.7128, -74.0060), tiles="cartodb positron")

folium.GeoJson(
    br_map,
    marker=folium.Circle(radius=4, fill_color="orange", fill_opacity=0.4, color="black", weight=1),
    tooltip=folium.GeoJsonTooltip(fields=["Location", "Hours", "Open"]),
    popup=folium.GeoJsonPopup(fields=["Location", "Hours", "Open"]),
    highlight_function=lambda x: {"fillOpacity": 0.8},
    zoom_on_click=True,
).add_to(geo_map)

url = "./geojson.html"

geo_map.save(url)