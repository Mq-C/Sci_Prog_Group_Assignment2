import geopandas as gpd
import rasterio
from rasterio.mask import mask
import numpy as np
from shapely.geometry import Point
import pandas as pd
import os
from typing import Tuple

def prepare_layers(csv_path:str, 
                            flood_extent_path:str,
                            roads_path:str,
                            target_crs:int= 3177)->Tuple[gpd.GeoDataFrame,gpd.GeoDataFrame,gpd.GeoDataFrame]:
    """
    Load and validate vector layers 
    This function prepares the buildings points from csv, then flood extent polygon, roads,make
    sure they have the same crs and valid geometries

    Parameters
    ----------
        csv_path: path to the input csv file
        flood_extent_shp_path: path to flood extent vetor
        road_path: path to roads vector file
        target_crs: the crs used in this project, defaults to 3177

     Returns
     -------
        A tuple containing flood_extent_shp, buildings,roads as GeoDataFrames

    Raises
    ------
        AssertionError if geometries are invalid,empty or outside Derna boundary
    """
    if not os.path.exists(csv_path):
        raise FileNotFoundError(f'building csv file no found')
    
    df = pd.read_csv(csv_path).copy(deep=True)
    geometry= [Point(xy) for xy in zip(df['longitude'],df['latitude'])]
    buildings_original= gpd.GeoDataFrame(df,geometry =geometry,crs =4326)
    buildings = buildings_original.copy(deep=True)

    bounds= buildings.total_bounds
    if not (bounds[0]>20 and bounds[2]<25):
         raise AssertionError(f"Building points (xmin:{bounds[0]}) are outside Derna bounds (20-25E)")

    flood_shp = gpd.read_file(flood_extent_path).copy(deep=True)
    roads = gpd.read_file(roads_path).copy(deep=True)
    
    layers = {'Flood extent': flood_shp,'Buildings':buildings,'Roads':roads}
    for name,gdf in layers.items():
        if gdf.crs is None or gdf.crs.to_epsg() != target_crs:
            layers[name] = gdf.to_crs(epsg=target_crs)
        
        if not layers[name].is_valid.all():
                layers[name].geometry = layers[name].geometry.buffer(0)

        if len(layers[name])==0:
             raise AssertionError(f'{name} layer is empty')

    return layers['Flood extent'],layers['Buildings'],layers['Roads']



