#!/usr/bin/env python3

# TODO: Jupyter Notebook

# interactive plotting  using folium library
import folium

map = folium.Map(location=[50.0, 14.0], tiles='OpenStreetMap', zoom_start=9)
map

# TODO: update
# Create a geometry list from the GeoDataFrame
geo_df_list = [[point.xy[1][0], point.xy[0][0]] for point in geo_df.geometry ]

# Iterate through list and add a marker.
i = 0
for coordinates in geo_df_list:
    if geo_df.type[i] == "Glenmore Water Treatment Plant":
        type_color = "green"
    elif geo_df.type[i] == "Richmond - Knob Hill Community Hall":
        type_color = "blue"
    elif geo_df.type[i] == "Richmond - Knob Hill Community Hall":
        type_color = "orange"
    elif geo_df.type[i] == "Bearspaw Water Treatment Plant ":
        type_color = "pink"
    else:
        type_color = "purple"


    # Place the markers with the popup labels and data
    map.add_child(folium.Marker(location = coordinates,
                            popup =
                            "Coordinates: " + str(geo_df_list[i]),
                            icon = folium.Icon(color = "%s" % type_color)))
    i = i + 1

map
