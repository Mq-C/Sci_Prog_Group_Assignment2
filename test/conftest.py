import numpy as np
import pytest
import geopandas as gpd
from shapely.geometry import Polygon, Point, LineString
import rasterio
from rasterio.transform import from_origin


@pytest.fixture
def target_crs():
    # What you EXPECT
    return 3177


@pytest.fixture
def flood_extent():
    # Intentionally WRONG CRS (EPSG:4326) so the CRS check fails
    poly = Polygon([(0, 0), (1, 0), (1, 1), (0, 1)])
    return gpd.GeoDataFrame({"id": [1]}, geometry=[poly], crs="EPSG:4326")


@pytest.fixture
def roads():
    # Intentionally WRONG geometry type: points instead of lines (will fail geometry type check)
    pts = [Point(0, 0), Point(1, 1)]
    return gpd.GeoDataFrame({"id": [1, 2]}, geometry=pts, crs="EPSG:4326")


@pytest.fixture
def buildings():
    # CRS also wrong + bounds not in 20..25E, so the Derna-bounds check fails too
    pts = [Point(10, 10), Point(11, 11)]
    return gpd.GeoDataFrame({"id": [1, 2]}, geometry=pts, crs="EPSG:4326")


@pytest.fixture
def pop_raster_path(tmp_path):
    # Create a small raster on disk with WRONG CRS so raster CRS check fails
    path = tmp_path / "pop.tif"
    data = np.ones((1, 10, 10), dtype=np.uint8)
    transform = from_origin(0, 10, 1, 1)

    with rasterio.open(
        path,
        "w",
        driver="GTiff",
        height=data.shape[1],
        width=data.shape[2],
        count=1,
        dtype=data.dtype,
        #crs="EPSG:4326",  # intentionally wrong
        transform=transform,
    ) as dst:
        dst.write(data)

    return str(path)


# Fixtures for the clipping tests (also intentionally "wrong")
@pytest.fixture
def original_buildings(buildings):
    return buildings


@pytest.fixture
def clipped_buildings(buildings):
    # Intentionally NOT clipped (same length) -> should fail "filtered out" assertion
    return buildings.copy()


@pytest.fixture
def original_roads():
    # Proper line roads for this test
    lines = [LineString([(0, 0), (10, 0)]), LineString([(0, 0), (0, 5)])]
    return gpd.GeoDataFrame({"id": [1, 2]}, geometry=lines, crs="EPSG:4326")


@pytest.fixture
def clipped_roads(original_roads):
    # Intentionally distorted: make longer than original -> should fail
    lines = [LineString([(0, 0), (100, 0)])]
    return gpd.GeoDataFrame({"id": [1]}, geometry=lines, crs=original_roads.crs)


@pytest.fixture
def original_pop_array():
    return np.ones((100, 100), dtype=np.uint8)


@pytest.fixture
def clipped_pop_array():
    return np.ones((50, 50), dtype=np.uint8)


@pytest.fixture
def flood_extent_array():
    # Intentionally different shape so it fails
    return np.ones((60, 60), dtype=np.uint8)
