import pandas as pd

import os
print(os.listdir())

df = pd.read_csv('datasets\inputs\open_buildings_v3_polygons_your_own_wkt_polygon_derna.csv.gz')

import pandas as pd
import geopandas as gpd
from shapely.geometry import Point
import matplotlib.pyplot as plt

# df already loaded from your CSV
# df = pd.read_csv("...")

# 1. Make sure coords are numeric and not missing
df = df.dropna(subset=['longitude', 'latitude'])
df['longitude'] = pd.to_numeric(df['longitude'])
df['latitude']  = pd.to_numeric(df['latitude'])

# 2. Build GeoDataFrame with POINT geometries
gdf_points = gpd.GeoDataFrame(
    df,
    geometry=gpd.points_from_xy(df['longitude'], df['latitude']),
    crs="EPSG:4326"   # WGS84 lat/lon
)

print("Number of points:", len(gdf_points))

# 3. Plot
ax = gdf_points.plot(figsize=(8, 8), markersize=1)
plt.tight_layout()
plt.show()