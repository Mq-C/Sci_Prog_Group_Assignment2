import geopandas as gpd
import os
import numpy as np
import torch

def clip_vectors_numpy(exposure_gdf:gpd.GeoDataFrame,mask_gdf:gpd.GeoDataFrame):
    """
    This functions clip vector layers (buildings and roads) to a mask (flood extent) using Numpy

    Parameters
    ==========
    exposure_gdf: buildings and roads
    mask_gdf: flood extent

    Returns
    =======
    A clipped GeodataFrame contaings only features within the mask
    """
    if exposure_gdf.crs != mask_gdf.crs:
        print(f'Convert exposure layer crs to {mask_gdf.crs}')
        exposure_gdf = exposure_gdf.to_crs(mask_gdf.crs)

    clipped_gdf= gpd.clip(exposure_gdf,mask_gdf)
    
    return clipped_gdf.copy()


def clip_vectors_tensor(exposure_gdf:gpd.GeoDataFrame,mask_gdf:gpd.GeoDataFrame):
    """
    This functions clip vector layers (buildings and roads) to a mask (flood extent) using Pytorch tensor

    Parameters
    ==========
    exposure_gdf: buildings and roads
    mask_gdf: flood extent

    Returns
    =======
    A clipped GeodataFrame contaings only features within the mask
    """
    coords_np = np.array([[geom.centroid.x, geom.centroid.y] for geom in exposure_gdf.geometry])
    coords_t = torch.from_numpy(coords_np)
    bounds_t = torch.tensor(mask_gdf.total_bounds)

    mask_x = torch.logical_and(coords_t[:, 0] >= bounds_t[0], coords_t[:, 0] <= bounds_t[2])
    mask_y = torch.logical_and(coords_t[:, 1] >= bounds_t[1], coords_t[:, 1] <= bounds_t[3])
    bbox_mask = torch.logical_and(mask_x, mask_y)

    # Filter to candidates within the box
    candidates = exposure_gdf.iloc[bbox_mask.numpy()].copy()

    # 2. PRECISE STEP: Actual Geometric Clip (Removes points in the 'dry' corners of the box)
    # This ensures only features touching the actual flood water are kept
    final_clipped = gpd.clip(candidates, mask_gdf)
    
    return final_clipped
    

    
