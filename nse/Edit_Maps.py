import folium
import geopandas as gpd
import os

name = 'NSE_Aguascalientes'
file_name = name + '.json'
html_name = name + '.html'
geojson_file = os.path.join(os.curdir, file_name)
gdf = gpd.read_file(geojson_file)

center_coords = (21.8819, -102.2916)  ## COORDENADAS

m = folium.Map(location=center_coords, zoom_start=12) ## ZOOM

folium.Marker(location=center_coords).add_to(m)

for i, feature in enumerate(gdf['geometry']):
    clase = gdf['NIVEL PREDOMINANTE'][i]

    clase_color = {'A/B': '#00FF00', 'C+': '#CBFF00', 'C': '#E5FF00', 'C-': '#FFE100', 'D+': '#FFA500', 'D': '#FF8200', 'E': '#FF0000'}
    color = clase_color.get(clase, '#00000000')

    if feature.geom_type == 'Polygon':
        scaled_coordinates = [[y, x] for x, y in zip(feature.exterior.xy[0], feature.exterior.xy[1])]
        folium.Polygon(locations=scaled_coordinates, fill_color=color, fill_opacity=0.7, stroke=False).add_to(m)

    elif feature.geom_type == 'MultiPolygon':
        for polygon in feature.geoms:
            scaled_coordinates = [[y, x] for x, y in zip(polygon.exterior.xy[0], polygon.exterior.xy[1])]
            folium.Polygon(locations=scaled_coordinates, fill_color=color, fill_opacity=0.7, stroke=False).add_to(m)

output_html = f'{os.path.splitext(file_name)[0]}.html'
m.save(output_html)