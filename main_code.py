import matplotlib.pyplot as plt
import os
import rasterio
from functions.prepare_layers import prepare_layers
from functions.vector_clipping import clip_vectors_numpy, clip_vectors_tensor
from functions.raster_clipping import clip_raster_numpy,sample_depth_at_buildings,clip_raster_tensor

csv_path = r'datasets\inputs\open_buildings_v3_polygons_your_own_wkt_polygon_derna.csv.gz'
flood_path = r'datasets\inputs\PHR_20230913_FloodExtent_Derna.shp'
roads_path = r'datasets\inputs\Road.shp'
water_depth_path = r'datasets\inputs\EMSN177_FLEX_AOI01_P01MODFL01_maxWaterDepth_v01.tif'
pop_2020_path = r'datasets\inputs\lby_pop_2020_CN_100m_R2025A_v1.tif'
pop_2024_path= r'datasets\inputs\lby_pop_2024_CN_100m_R2025A_v1.tif'
output_folder = 'outputs'
os.makedirs(output_folder, exist_ok=True)

clipped_buildings_path = os.path.join(output_folder, 'clipped_buildings.gpkg')
clipped_roads_path = os.path.join(output_folder, 'clipped_roads.gpkg')

def plot_exposure(flood_gdf,infrastructure_gdf,impacted_gdf,title,save_name,color):
    save_path = os.path.join(output_folder,save_name)
    if os.path.exists(save_path):
        print(f"Overwriting existing map: {save_name}")
    
    fig,ax= plt.subplots(figsize=(10,10))

    flood_gdf.plot(ax=ax,edgecolor='cyan',facecolor='none',alpha=0.2,label='Flood Extent')
    infrastructure_gdf.plot(ax=ax, color = 'black',alpha=0.3,markersize=1,linewidth = 0.5,label = "Total infrastructures")
    impacted_gdf.plot(ax=ax, color =color, markersize=4,linewidth=1.5, label='Exposed infrastructures')
    
    xmin, ymin, xmax, ymax = flood_gdf.total_bounds
    buffer = 500 
    ax.set_xlim(xmin - buffer, xmax + buffer)
    ax.set_ylim(ymin - buffer, ymax + buffer)

    ax.set_title(title, fontsize=14, fontweight='bold')
    ax.set_xlabel("Easting (m)")
    ax.set_ylabel("Northing (m)")
    ax.legend(loc='lower right')
    
    plt.savefig(save_path, dpi=300, bbox_inches='tight')
    plt.close(fig) 
    print(f"Map saved successfully at: {save_path}")
    plt.show()


def main():
    flood,buildings,roads = prepare_layers(csv_path,flood_path,roads_path)

    #vector clippping outputs
    impacted_buildings_np = clip_vectors_numpy(buildings,flood)
    impacted_roads_t = clip_vectors_tensor(roads,flood)
    

    #raster clipping outputs
    water_depth_array, water_depth_meta = clip_raster_numpy(water_depth_path,flood)
    water_depth_output = os.path.join(output_folder,'clipped_water_depth.tif')
    with rasterio.open(water_depth_output,'w',**water_depth_meta) as dst:
        dst.write(water_depth_array,1)

    pop_array_2020, pop_meta_2020 = clip_raster_tensor(pop_2020_path,flood)
    pop_array_2024, pop_meta_2024 = clip_raster_tensor(pop_2024_path,flood)

    pop_output_2024 = os.path.join(output_folder,'clipped_population_2024.tif')
    with rasterio.open(pop_output_2024,'w',**pop_meta_2024) as dst:
        dst.write(pop_array_2024,1)

    pop_output_2020 = os.path.join(output_folder,'clipped_population_2020.tif')
    with rasterio.open(pop_output_2020,'w',**pop_meta_2020) as dst:
        dst.write(pop_array_2020,1)

    impacted_buildings = sample_depth_at_buildings(impacted_buildings_np,water_depth_output)

    buildings_gpkg = os.path.join(output_folder,'impacted_buildings_with_water_depth.gpkg')
    roads_gpkg = os.path.join(output_folder,'impacted_roads.gpkg')

    for path, gdf, name in [(buildings_gpkg, impacted_buildings, "Buildings"), (roads_gpkg, impacted_roads_t, "Roads")]:
        if os.path.exists(path):
            os.remove(path)
        gdf.to_file(path, driver='GPKG')
        print(f"-> {name} layer saved to {path}")


    plot_exposure(flood,buildings,impacted_buildings_np,
                  'Derna Flood: Buildings Exposure (Numpy)',
                  'buildings_exposure.png','red')
    
    plot_exposure(flood,roads,impacted_roads_t,
                  'Derna Flood: Roads Exposure (Tensor)',
                  'roads_exposure.png','red')








if __name__ == "__main__":
    main()