import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
os.environ.pop("PROJ_LIB", None)
import numpy as np
import pytest
import geopandas as gpd
from shapely.geometry import Polygon, Point, LineString
import rasterio
from rasterio.transform import from_origin


@pytest.fixture
def target_crs():
    return 3177


@pytest.fixture
def flood_extent():
    poly = {'id':[1],'geometry': [Polygon([(0, 0), (1000, 0), (1000, 1000), (0, 1000)])]}
    return gpd.GeoDataFrame(poly,crs="EPSG:3177")


@pytest.fixture
def roads():
    roads = {'id':[1,2],
             'geometry':[LineString([(0,0),(1,1)]),LineString([(1,1),(2,2)])]}
    return gpd.GeoDataFrame(roads, crs="EPSG:3177")
@pytest.fixture
def original_roads():
    roads = {'id': [1, 2], 
            'geometry': [LineString([(0, 0), (10, 0)]), LineString([(0, 0), (0, 5)])]}
    return gpd.GeoDataFrame(roads, crs="EPSG:3177")

@pytest.fixture
def clipped_roads():
    lines = [LineString([(0,0),(5,0)])]
    return gpd.GeoDataFrame({'id':[1]},geometry = lines,crs='EPSG:3177')

@pytest.fixture
def buildings(target_crs):
    buildings = {'id':[1,2],'geometry': [Point(22.1,32.7),Point(22.3,32.8)]}
    gdf_4326 = gpd.GeoDataFrame(buildings,crs='EPSG:4326')
    return gdf_4326.to_crs(epsg=target_crs)

@pytest.fixture
def original_buildings():
    return gpd.GeoDataFrame({'id':[1,2],'geometry': [Point(100,100),Point(200,200)]},crs=3177)

@pytest.fixture
def clipped_buildings():
    return gpd.GeoDataFrame({'id':[1],'geometry': [Point(10,10)]},crs=3177)

@pytest.fixture
def flood_extent_array():
    return np.ones((50,50),dtype='uint8')

@pytest.fixture
def original_pop_array():
    return np.ones((100,100),dtype='uint8')
@pytest.fixture
def clipped_pop_array():
    return np.ones((50,50),dtype='uint8')    


@pytest.fixture
def pop_raster_path(tmp_path,target_crs):
    path = tmp_path / "pop.tif"
    data = np.ones((1, 10, 10), dtype='uint8')
    transform = from_origin(0, 10, 1, 1)

    with rasterio.open(
        str(path),
        "w",
        driver="GTiff",
        height=data.shape[1],
        width=data.shape[2],
        count=1,
        dtype='uint8',
        crs=f"EPSG:{target_crs}",
        transform=transform,
    ) as dst:
        dst.write(data)

    return str(path)
