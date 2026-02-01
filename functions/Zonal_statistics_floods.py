# Import the main libraries

import os
import numpy as np
import pandas as pd
import geopandas as gpd
import fiona
from pyproj import CRS
import matplotlib.pyplot as plt
import folium
import rasterio
from affine import Affine
from tabulate import tabulate
import xarray as xr
import rioxarray
import math

# Importing a file and converting a gdf 

### Function which returned a geodataframe from a geopackage o GeoJSON file and print the head, the inputs are the path of the geopackage or geojson file
### and the layer inside the geopackage


def create_gdf(path, layer=None):
    '''
    The function reads a geopackage or geojson and convert it into a GeoDataFrame.
    
    parameters: 
        path (str): Path to the geopackage file.
        layer (str): If the geopackage has different layers, specify the layer to open, otherwise layer = None.
    
    Print:
        print(gdf_head): It prints the first five rows for the geodataframe as a reference.
        
    Returns:
        gdf (GeoDataFrame): It contains the GeoDataFrame with all the information in the geopackage or geojson file.
        gdf_head (GeoDataFrame): It contains the first rows in the gdf, they are ready to print. 
    
    Raises: 
        FileNotFoundError: It will raise, if the path does not exist or it is wrong.
        ValueError: It will raise, if the file cannot be read by geopandas because the name of the layers.
    '''
    
    if not os.path.exists(path):
            raise FileNotFoundError(f'The file does not exist or the path is wrong:{path}')
    
    if path.lower().endswith(".gpkg"):
        layers = fiona.listlayers(path)
        
        if layer is None:
             raise ValueError(f'geopackage contains multiple layers: {layers}, specify the layer to read')
        
        if layer not in layers:
            raise ValueError(f'layer {layer} not found. Available leyers:{layers}')
        
    try:    
        gdf = gpd.read_file(path, layer=layer)   # This part was fixed update the code 
        gdf_head = gdf.head()
        
    except Exception as e:
        # Raise a error if for any reason geopandas cannot read the geopackage
        raise ValueError(f'Error reading the file {path}: {e}')
    
    
    return gdf

# Function to validate the CRS project in Derna (3177) in a GeoDataFrame and if the CRS is not that, it will be reprojected to this CRS project. (function assignment 1)

def check_crs_3177(gdf):
    '''
    The function reads a GeoDataFrame and considerer a predefine CRS based on EPSG for the project then it reads the current crs and if 
    this is different from the defined parameter, it will reproject the geodataframe.
    
    parameters: 
        gdf (geodataframe): GeoDataFrame to validate and set the coordinate system
    
    Print:
        print(crs_initial): It prints the original CRS for the geodataframe.
        print(crs_final): It prints the final CRS for the geodataframe after verification.
        
    Returns:
        gdf (GeoDataFrame): It contains the GeoDataFrame with the CRS setup for the project after verification.
            
    Raises: 
        ValueError: It will raise, if the GeoDataFrame does not have a CRS defined.
    '''
    
    if gdf.crs is None:
        raise ValueError("NO CRS defined.")
    crs_initial = gdf.crs
    
    # Set the CRS target for the project
    target_crs = CRS.from_epsg(3177)
    
    # Set the CRS for the project in case it is different to the target.
    if gdf.crs != target_crs:
        gdf = gdf.to_crs(target_crs)    # I suggest this improvement
        
    print(f'Initial CRS: {crs_initial}') 
    print(f'Final CRS: {gdf.crs}') 
    return gdf

## Function to report the total the affected roads and the total length by categories and plotting

def road_statistics(gdf):
    # First part computing the road length (km)
    roads_affected = gdf['Shape__Len'].sum() / 1000    # Report the value in km
    print(f'Total length of roads affected by the floods: {roads_affected:.2f} km')
    
    # Plotting the road length by type
    gdf['fclass'] = gdf['fclass'].str.strip().str.title()  # Formating the text on the x - axis
    roads_affected_type = gdf.groupby('fclass')['Shape__Len'].sum() / 1000    # Report the value in km
    ax = roads_affected_type.plot(kind = 'bar', figsize=(8,5), color='green', edgecolor= 'black')
    ax.set_xlabel('Road class', fontsize=12, fontweight=2)
    ax.set_ylabel('Road length (km)', fontsize=12, fontweight=2)
    ax.set_title('Total road length by type affected by Derna Floods', fontsize=18, fontweight=2)
    for i, value in enumerate(roads_affected_type):
        ax.text(i, value, f'{value:.2f}', ha='center', va='bottom')
    plt.tight_layout()
    plt.show()
    
## Function to report the total number of affected buildings, the density of the buildings inside the flood extent and the status for the 
# buildings based on condition determined by the water depth

def Buildings_statistics(gdf1, gdf2):
    # Compute the number of the buildings affected by the floods 
    Buildings_affected = gdf1['geometry'].count()
    print(f'Total number of buildings affected by the floods: {Buildings_affected:.0f}')
    # Compute the density of the buildings inside the flood extent
    area= gdf2.geometry.area
    area_km2 = area / pow(1000,2)
    density = Buildings_affected/area_km2
    print(f'Density of the buildings affected by the floods: {density.iloc[0]:.0f} buildings/km^2')
    # Plot the buldings status based on the waterdepth condition
    gdf1['status'] = gdf1['status'].str.strip().str.title()  # Formating the text on the x - axis
    Buildings_affected_type = gdf1.groupby('status')['geometry'].count()
    ax = Buildings_affected_type.plot(kind = 'bar', figsize=(8,5), color='green', edgecolor= 'black')
    ax.set_xlabel('Building affectation', fontsize=12, fontweight=2)
    ax.set_ylabel('Number of buildings', fontsize=12, fontweight=2)
    ax.set_title('Status of the buildings affected by Derna Floods', fontsize=18, fontweight=2)
    for i, value in enumerate(Buildings_affected_type):
        ax.text(i, value, f'{value:.0f}', ha='center', va='bottom')
    plt.tight_layout()
    plt.show()
    
# Define the funtion to compute the statistics
def Population_statistics(path, year, flood):
    
    # Open the raster file using rasterio
    with rasterio.open(path) as src:
        
        # Read the data into a NumPy array
         population_array = src.read(1)  # Reads the first band of the raster
         
        ## Area of the flood extent in km^2
         area= flood.geometry.area
         area_km2 = area / pow(1000,2)
         
         ## Computing basic statistics 2020
         population_sum = round(np.nansum(population_array),0)  # Sum of population in the array
         population_dens = round(population_sum/area_km2,0)   # Density of population in the array
         population_mean = round(np.nanmean(population_array),0)  # Mean population in the array
         population_min = round(np.nanmin(population_array),0)  # Minimum population  in the array
         population_max = round(np.nanmax(population_array),0)  # Maximum population in the array
         
         # create a dictionary to include the information
         Population = {"Total population": population_sum,
                   "Population density (habitants/km^2)": population_dens[0],
                   "Mean population": population_mean,
                   "Minimum population": population_min,
                   "Maximum population":population_max}
         
         # Define the column names
         columns = ['Statistic', 'Value']
         
         # Convert the dictorionary to a dataframe
         Population_sta_df = pd.DataFrame(list(Population.items()), columns=columns)
         print(f'Basic statistics population: {year}\n')
         print(tabulate(Population_sta_df, headers='keys', tablefmt='fancy_grid', showindex=False, colalign=("center", "center")))
         
## Function to create and manipulate datacubes datasets population

# Define the function
def create_population_cube(dict):
    # Create a list to concantenate the xarrays
    concant_arrays=[]
    
    for key, value in dict.items():
        # load the raster files as xarray
        population_xarray = rioxarray.open_rasterio(key)
    
        # Print basic information (for each iteration is going to print i think it is not neccesary)
        print(f' Size dataArray: {population_xarray.sizes}')
        print(f' CRS dataArray: {population_xarray.rio.crs.to_epsg()}')
        print(f' resolution dataArray: {population_xarray.rio.resolution()}')
             
        # Remove the dimension band and reeplace with time
        population_xarray = population_xarray.squeeze("band").expand_dims(time=[pd.Timestamp(f"{value}-01-01")])
        concant_arrays.append(population_xarray)
    
    # Create the data cube using concat because they are the same variable 'time' in this case we are creating an Array
    population_cube = xr.concat(concant_arrays, dim="time")
    
    # outdate the attributes for the datacube # temporal coverage convert automatic

    population_cube.attrs.update({'title': 'Population inside the flood extent Derna, Lybia',
                              'Source information' : 'WorldPop - https://data.humdata.org/dataset/worldpop-population-counts-2015-2030-lby',
                              'temporal coverage': '2020 - 2021',
                              'time resolution': 'annual',
                              'note': 'Each band in the source corresponds to one year'})
    
    # Print basic information
    print(f' Dimensions Datacube: {population_cube.dims}')
    return population_cube

## Create a funtion to plot the basic statistics through the datacube (xarray)

def Population_statistics_cube(xarray, flood):
    # create a empty dataframe
    Population_stats_all = pd.DataFrame()
    years_analysis = []
    for t in xarray.time:
        # compute the basic statistics
        population_sum = xarray.sel(time=t).sum(dim=('y', 'x')).round(0)
        population_mean = xarray.sel(time=t).mean(dim=('y', 'x')).round(0)
        population_max = xarray.sel(time=t).max(dim=('y', 'x')).round(0)
        population_min = xarray.sel(time=t).min(dim=('y', 'x')).round(0)
        
        ## Area of the flood extent in km^2
        area= flood.geometry.area
        area_km2 = area / pow(1000,2)
        #population_dens
        population_dens = int(round(population_sum.item()/float(area_km2.iloc[0]),0))
        
        
        # create a dictionary to include the information
        Population = {"Total population": population_sum,
                   "Population density (habitants/km^2)": population_dens,
                   "Mean population": population_mean,
                   "Minimum population": population_min,
                   "Maximum population":population_max}
        
        # convert the dictionary to a series with the name = year
        year = pd.Timestamp(t.item()).year
        years_analysis.append(year)
        Population_series = pd.Series(Population, name=str(year))
        
        # Add the new dataframe to the general dataframe
        Population_stats_all = pd.concat([Population_stats_all, Population_series], axis=1)
    
    # Reset index to have a column for statistics
    Population_stats_all = Population_stats_all.rename_axis("Statistic").reset_index()
    
    # print the outputs
    print(f'Basic statistics population: {years_analysis[0]} - {years_analysis[len(years_analysis)-1]}\n')
    print(tabulate(Population_stats_all, headers='keys', tablefmt='fancy_grid', showindex=False, colalign=("center", "center")))
    
# Function to plot in a plan view the population based on the pixel value

def plot_population(xarray):
    n = xarray.sizes['time']
    rows = math.ceil(n)
    cols = 3
    years_analysis = []
    
    # Define the figure
    fig, axes = plt.subplots(rows,cols, figsize=(12,4*rows))
    axes = axes.flatten()
    
    # Loop through i, t to plot each time
    for i, t in enumerate(xarray.time):
        ax = axes[i]     
        xarray.sel(time=t).plot(ax=ax, cbar_kwargs={'label': 'Pixel Population'})
        year = pd.to_datetime(t.values).year
        ax.set_title(f'Population {year} inside flood extent')
        ax.set_xlabel('X')
        ax.set_ylabel('Y', rotation=0, labelpad=10)
        years_analysis.append(year)
        
    # Detele Empty plots 
    for j in range (i+1, len(axes)):
        fig.delaxes(axes[j])
        
    #Set configuration plots 
    fig.suptitle(f"Population inside flood extent over {years_analysis[0]} - {years_analysis[len(years_analysis)-1]}", fontsize=18, fontweight="bold", y=1)
    plt.tight_layout()
    plt.show()
    
# Function to plot a time series for the population through the years

def plot_series_population(xarray, flood):
    
    # Total population
    population_total = xarray.sum(dim=('y', 'x')).round(0)
    population_total = population_total.assign_coords(time=population_total['time'].dt.year.astype(str))
    years = population_total['time'].values
    year_first = years[0]
    year_last= years[-1]
    
    # Density population
    ## Area of the flood extent in km^2
    area= flood.geometry.area
    area_km2 = area / pow(1000,2)
    population_dens_list = []
    
    for t in xarray.time:
        pop_total = xarray.sel(time = t).sum(dim=('y', 'x')).round(0)
        dens = int(round(pop_total.item()/float(area_km2.iloc[0]),0))
        population_dens_list.append(dens)
        
    # Plotting
    fig, axes = plt.subplots(1,2, figsize=(16,5))
    
    # Plot Total population
    population_total.plot(ax=axes[0], marker = 'o')
    axes[0].set_ylabel('Total population', fontsize=14)
    axes[0].set_xlabel('Year', fontsize=14)
    axes[0].set_title(f'Population inside flood extent over {year_first } - {year_last}', fontsize=18, fontweight='bold')
    axes[0].grid(True)
    
    # Plot population Density
    axes[1].plot(years, population_dens_list, marker = 'o')
    axes[1].set_ylabel('Habitants/km^2', fontsize=14)
    axes[1].set_xlabel('Year', fontsize=14)
    axes[1].set_title(f'Population Density  inside flood extent over {year_first } - {year_last}', fontsize=18, fontweight='bold')
    axes[1].grid(True)
    
    plt.tight_layout()
    plt.show()