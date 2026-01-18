import geopandas as gpd
import rasterio
from rasterio.mask import mask
import numpy as np
<<<<<<< HEAD
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
=======
from shapely.geometry import box
import pandas as pd
import os
from typing import Tuple,Union

def buildings_csv_to_points(csv_path:str, crs:Union[int,str]= 3177)->gpd.GeoDataFrame:
    """
    Convert building csv with lon/lat to a point GeoDataFrame
>>>>>>> 4ee6104e7947d8fb88bf5818e7dec894b25dd534

    Parameters
    ----------
        csv_path: path to the input csv file
<<<<<<< HEAD
        flood_extent_shp_path: path to flood extent vetor
        road_path: path to roads vector file
        target_crs: the crs used in this project, defaults to 3177

     Returns
     -------
        A tuple containing flood_extent_shp, buildings,roads as GeoDataFrames

    Raises
    ------
        AssertionError if geometries are invalid,empty or outside Derna boundary
=======
        lat_col: column name for latitude values
        lom_col:column name for longitude values

     Returns
     -------
        GeoDataFrame with point Geometry

    Raises
    ------
        FileNotFoundError if the input file is missing
        KeyError if lon/lat columns are not in thet csv
        ValueError if failed to create the GeoDataFrame
>>>>>>> 4ee6104e7947d8fb88bf5818e7dec894b25dd534
    """
    if not os.path.exists(csv_path):
        raise FileNotFoundError(f'building csv file no found')
    
    df = pd.read_csv(csv_path).copy(deep=True)
<<<<<<< HEAD
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


=======
    cols = ['longitude','latitude']
    missing_cols = [col for col in cols if col not in df.columns]
    if missing_cols:
        raise KeyError(f'csv missing required columns')
    
    try:
        gdf = gpd.GeoDataFrame(df,geometry= gpd.points_from_xy(df['longitude'],df['latitude']), crs = crs)
    except Exception as e:
        raise ValueError(f'failed to create geodataframe: {str(e)}')
    
    return gdf

def prepare_layers(flood_extent_shp:gpd.GeoDataFrame,
                   buildings: gpd.GeoDataFrame,
                   roads: gpd.GeoDataFrame,
                   pop_raster_path:str,
                   target_crs:int) -> Tuple[gpd.GeoDataFrame, gpd.GeoDataFrame,gpd.GeoDataFrame,str]:
    
    flood_shp_copy = flood_extent_shp.copy(deep=True)
    buildings_copy = buildings.copy(deep=True)
    roads_copy = roads.copy(deep=True)
    
    assert flood_shp_copy.geom_type.isin(['Polygon']).all(),'Flood extent shp msut be polygon'
    assert buildings_copy.geom_type.isin(['Point']).all(),'Buildings extent shp msut be points'
    assert all(isinstance(geom,(gpd.points_from_xy,type(None))) is False for geom in flood_extent_shp.geometry),\
        'Flood extent shp must be polygon'
    assert all(isinstance(geom,(gpd.lonestrings_from_xy,type(None))) is False for geom in roads.geometry),\
        'Roads must be Linestring'
    assert all(isinstance(geom,(gpd.points_from_xy,type(None))) is False for geom in buildings.geometry),\
        'Buildings must be poitns'

    flood_extent_shp = flood_extent_shp.t
>>>>>>> 4ee6104e7947d8fb88bf5818e7dec894b25dd534

