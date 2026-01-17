import matplotlib.pyplot as plt
import os
from functions.prepare_layers import buildings_csv_to_points

csv_path = r'datasets\inputs\open_buildings_v3_polygons_your_own_wkt_polygon_derna.csv.gz'
output_folder = 'outputs'



buildings_gdf = buildings_csv_to_points(csv_path)
output_path = os.path.join(output_folder,'Buildings point shp')
buildings_gdf.to_file(output_path,driver='GPKG')
print(f'building geodataframe saved to outputs')
fig, ax = plt.subplots(figsize=(10, 10))
buildings_gdf.plot(ax=ax, color='blue', markersize=5, alpha=0.6)
    
 # Set titles for your report
ax.set_title("Distribution of Buildings in Derna, Libya", fontsize=15)
ax.set_xlabel("Longitude")
ax.set_ylabel("Latitude")
ax.grid(True, linestyle='--', alpha=0.5)
plt.show()
