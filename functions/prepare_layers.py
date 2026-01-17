import geopandas as gpd
import rasterio
from rasterio.mask import mask
import numpy as np
from shapely.geometry import box
import pandas as pd
import os
from typing import Tuple,Union

def buildings_csv_to_points(csv_path:str, crs:Union[int,str]= 3177)->gpd.GeoDataFrame:
    """
    Convert building csv with lon/lat to a point GeoDataFrame

    Parameters
    ----------
        csv_path: path to the input csv file
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
    """
    if not os.path.exists(csv_path):
        raise FileNotFoundError(f'building csv file no found')
    
    df = pd.read_csv(csv_path).copy(deep=True)
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

