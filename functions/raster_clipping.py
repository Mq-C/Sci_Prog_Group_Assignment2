import rasterio
from rasterio.mask import mask
import numpy as np
import torch
import geopandas as gpd
from typing import Tuple,Dict,Any

def clip_raster_numpy(raster_path:str,mask_gdf:gpd.GeoDataFrame)->Tuple[np.ndarray, Dict[str, Any]]:
    """
    This function clips a raster isomg a vector mask and processes pixel values usiong numpy

    Parameters
    ==========
    raster_path: file path to the input layer (water depth raster)
    mask_gdf: the flood extent polygon

    Returns
    =======
    A tupple containig the processed 2D numpy array,and
      updated metadata 
    """
    with rasterio.open(raster_path) as src:
        if mask_gdf.crs != src.crs:
            mask_gdf = mask_gdf.to_crs(src.crs)
        
        out_image, out_transform = mask(src,mask_gdf.geometry,crop=True)
        out_meta=src.meta.copy()

        raster_data = out_image[0].astype(np.float32)
        processed_data= np.where(raster_data<0 , 0, raster_data)
    
    out_meta.update({
        "height": processed_data.shape[0],
        "width": processed_data.shape[1],
        "transform": out_transform,
        "nodata": 0.0
    })
    return processed_data, out_meta

def clip_raster_tensor(raster_path:str,mask_gdf:gpd.GeoDataFrame)->Tuple[np.ndarray, Dict[str, Any]]:
    """
    This function clips a raster isomg a vector mask and processes pixel values usiong Pytorch
    it performs the geometric clip and then use torch.clamp to ensure all pixel values are non negative

    Parameters
    ==========
    raster_path: file path to the input layer (water depth raster)
    mask_gdf: the flood extent polygon

    Returns
    =======
    A tupple containig the processed 2D numpy array,and
      updated metadata 
    """
    with rasterio.open(raster_path) as src:
        if mask_gdf.crs != src.crs:
            mask_gdf = mask_gdf.to_crs(src.crs)
        
        out_image, out_transform = mask(src,mask_gdf.geometry,crop=True)
        out_meta=src.meta.copy()

        raster_data_t = torch.from_numpy(out_image[0].astype(np.float32))
        processed_data_t= torch.clamp(raster_data_t,min=0)
    
    out_meta.update({
        "height": processed_data_t.shape[0],
        "width": processed_data_t.shape[1],
        "transform": out_transform,
        "nodata": 0.0
    })
    return processed_data_t.numpy(), out_meta

def sample_depth_at_buildings(impacted_buildings_gdf:gpd.GeoDataFrame,raster_path:str,backend='numpy'):
    """
    This function extracts values at point locations and handles no data value

    Parameters
    ==========
    points_gdf: the impacted buildings gdf

    raster_path: path

    Returns
    =======
    A tupple containig the processed 2D numpy array of pixel values, 
    and the updated metadata dictionary for teh clipped raster
    """
    with rasterio.open(raster_path) as src:
        if impacted_buildings_gdf.crs != src.crs:
            impacted_buildings_gdf = impacted_buildings_gdf.to_crs(src.crs) 

        coords=[(x,y) for x,y in zip(impacted_buildings_gdf.geometry.x,impacted_buildings_gdf.geometry.y)]

        sampled_values = [val[0] for val in src.sample(coords)]

    impacted_buildings_gdf['water_depth'] =sampled_values
    impacted_buildings_gdf['status'] = np.where(impacted_buildings_gdf['water_depth']<=0,'Dry','Flooded')

    return impacted_buildings_gdf
