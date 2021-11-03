#https://geopandas.org/getting_started/introduction.html
#https://spatialreference.org/ref/epsg/?search=pulkovo&srtext=Search

import geopandas as gpd
import matplotlib.pyplot as plt

import logging
# add filemode="w" to overwrite
logging.basicConfig(level=logging.INFO)

logging.info('1')


'''
gdf2 = gpd.read_file("shapes/Adminbndy4.shp")
streets = gpd.read_file("shapes/Streets.shp")
logging.info('2')
streets_cp = gpd.read_file("shapes/Streets_clipped.shp")

logging.info('3')

#gdf['centroid'] = gdf.centroid
#gdf["area"] = gdf.area
#gdf["area"]

print(streets_cp.crs)

# gdf = gdf.set_geometry("centroid")
# gdf.plot("area", legend=True)

streets_cpproj = streets_cp.to_crs(epsg=3395)
logging.info('4')
streetsbuf=streets_cpproj['geometry'].buffer(distance=500)

streetsbuf = streetsbuf.to_crs(epsg=4326)

logging.info('5')

mask=streetsbuf
gdf=streets
logging.info('6')
#streets2=gpd.clip(gdf, mask, keep_geom_type=False)

logging.info('7')
#fig, ax = plt.sublots()
streets_cpproj.plot()
streetsbuf.plot()
#streets2.plot()
'''

'''
world = gpd.read_file(
    gpd.datasets.get_path('naturalearth_lowres'))
south_america = world[world['continent'] == "South America"]
capitals = gpd.read_file(
    gpd.datasets.get_path('naturalearth_cities'))
sa_capitals = gpd.clip(capitals, south_america)
'''

to_clip = gpd.read_file("shapes/Adminbndy5.shp")
mask = gpd.read_file("shapes/Streets.shp")
sa_capitals = gpd.clip(to_clip, mask)


sa_capitals.plot()


#ax = gdf["geometry"].plot()
#gdf["centroid"].plot(ax=ax, color="black")
plt.show()
#gdf.to_file("Adminbndy4.shp")
