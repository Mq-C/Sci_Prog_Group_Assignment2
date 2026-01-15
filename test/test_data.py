import geopandas as gpd
import rasterio
import numpy as np
from shapely.geometry import Polygon, LineString,Point
import pytest



def test_prepare_layers(flood_extent,buildings,pop_raster_path,roads,target_crs):

    #check geometry type
    assert all(isinstance(geom,(Polygon)) for geom in flood_extent.geometry),'Original flood extent must be polygon'
    assert all(isinstance(geom,(LineString)) for geom in roads.geometry), 'Roads must be lines'
    assert all(isinstance(geom, (Point)) for geom in buildings.geometry),'Buildings must be points'
    print('Geomtry for input data checked')

    #check crs
    layers = {"Flood_extent":flood_extent,'Roads':roads,'Building':buildings}
    for name, gdf in layers.items():
        assert gdf.crs.to_epsg() == target_crs,f"{name} is not in EPSG: {target_crs}"
    print('CRS checked')

    #check if geometry is valid
    for name, gdf in layers.items():
        invalid_count = (~gdf.is_valid).sum()
        assert invalid_count ==0, f'{name} has {invalid_count} invalid geometry'
    print('All geometries are valid')

    #check if a layer is empty
    for name,gdf in layers.item():
        assert len(gdf)>0, f'{name} layer is empty'
    print('The layer is not empty')

    #for raster layers: check if layer exist and not empty:
    with rasterio.open(pop_raster_path) as src:
        assert src.crs.to_epsg() == target_crs, f'Population raster is not correct'
        assert src.count>0,f'Population raster is empty'
    print('Raster layer checked')

    #check if building csv conversion worked and points are within Derna boundary
    #Derna boundary is approximately 20°E to 25°E
    assert buildings.total_bound[0]>20 and buildings.total_bound[2] <25, 'Building points are outside Derna'
    print('Building csv conversion to poitns worked')

def test_vector_clipping(original_buildings,clipped_buildings,original_roads,clipped_roads):
    #vector clipping

    ##number of building before and after clipping cannot be the same
    assert len(clipped_buildings) < len(original_buildings), 'No buildings were filtered out'
    assert len(clipped_buildings) >0, 'All buildings were deleted'
    print('Building clipping checked')

    ##the longest clipped road length cannot be longer than the original longest road
    assert clipped_roads.length.max() <= original_roads.length.max(),'Road geometry distorted'
    print('Road geometry checked')

def test_raster_clipping(original_pop_array,clipped_pop_array,flood_extent_array):
    assert clipped_pop_array.shape == flood_extent_array.shape,\
        'Clipped population must match flood extent'
    print('Clipped population matched flood extent')

    assert clipped_pop_array.size < original_pop_array.size,\
        'Population rastered was not clipped'
    

        



    


