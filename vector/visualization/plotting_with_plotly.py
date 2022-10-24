#!/usr/bin/env python3

# run from terminal: python3 ./vector/visualization/plotting_with_plotly.py
# or Jupyter notebook
# https://stackoverflow.com/questions/57211392/how-to-see-plotly-graphs-in-pycharm

import os
import pandas as pd
import geopandas as gpd
from shapely.geometry import Point, Polygon
import plotly.express as px

# data
os.listdir()
df = pd.read_csv("./geodata/vectors/cities.csv")
# df.head()

# create geometry
geometry=[Point(xy) for xy in zip(df['Y'], df['X'])]
# geometry[:1]
crs={'init': 'epsg:4326'}
gdf = gpd.GeoDataFrame(df, crs=crs, geometry=geometry)
# gdf.head()


# size='CONTINENT'
fig = px.scatter_geo(gdf, lat='Y', lon='X', color='POPULATION', 
                     projection="natural earth", basemap_visible=True,
                     title='Cities of the World')
fig.show()