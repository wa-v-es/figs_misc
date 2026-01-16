###
import numpy as np
# from numpy import load
import obspy
import miller_alaskamoho_srl2018 as alaskamoho
import cartopy
import cartopy.crs as ccrs
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
from cartopy.mpl.gridliner import LONGITUDE_FORMATTER, LATITUDE_FORMATTER
import cartopy.feature as cfeature
from obspy.clients.fdsn import Client
from obspy import read, Stream, UTCDateTime,read_events
import rasterio
import os.path as path
import stripy as stripy
import sys
from matplotlib.colors import ListedColormap
from scipy.interpolate import RegularGridInterpolator
#######
import cartopy.io.shapereader as shpreader
from shapely.geometry import Point

# Load Natural Earth country polygons
shp = shpreader.natural_earth(
    resolution='50m',
    category='cultural',
    name='admin_0_countries'
)
reader = shpreader.Reader(shp)

# Extract Canada geometry
canada = next(
    rec.geometry for rec in reader.records()
    if rec.attributes['NAME_LONG'] == 'Canada'
)

class Stations:
      def __init__(self,lat,lon):
            self.lat=lat
            self.lon=lon

sta_list=[]

with open('All.stations', "r") as infile:
        headerline = infile.readline() # ignore this one
        for line in infile:
            items = line.split()
            sta_list.append(Stations(float(items[3]),float(items[4])))

# boundaries = requests.get("https://raw.githubusercontent.com/fraxen/tectonicplates/master/GeoJSON/PB2002_boundaries.json").json()
cmap = plt.cm.RdYlBu
# Transparent colours
###
colA = cmap(np.arange(cmap.N))
colA[:,-1] = 0.25 + 0.5 * np.linspace(-1.0, 1.0, cmap.N)**2.0
#adjusts the opacity based on the quadratic curve, setting values between 0.25 and 0.75.
##
# Create new colormap
cmapA = ListedColormap(colA)
# cmapA = cmap
# proj = ccrs.Stereographic(central_longitude=-90, central_latitude=90, true_scale_latitude=55)
proj = ccrs.LambertConformal(
    central_longitude=-95,
    central_latitude=50,
    standard_parallels=(49, 77)
)
# plt.clf()
plt.ion()
fig = plt.figure(figsize=(15, 8), facecolor=None)
ax1 = plt.subplot(1, 1, 1, projection=proj)

plt.rcParams.update({'font.size': 14})

# ax1.gridlines(draw_labels=False, linewidth=0.5, color='gray', alpha=0.5)

ax1.set_extent([-136,-59,41,71], crs=ccrs.PlateCarree())

# grat = cartopy.feature.NaturalEarthFeature(category="physical", scale="10m", name="graticules_5")
# ax1.add_feature(grat, linewidth=0.5,linestyle="--",edgecolor="#000000",facecolor="None", zorder=2)

ax1.coastlines(resolution="50m",color="#111111", linewidth=0.5, zorder=99)
ax1.add_feature(cfeature.BORDERS.with_scale('50m'), linestyle=':')

ax1.add_feature(cartopy.feature.STATES.with_scale('50m'),linewidth=0.5,edgecolor='gray')
ax1.add_feature(cfeature.OCEAN.with_scale('50m'),alpha=0.1,facecolor='xkcd:azure')
# ax1.add_feature(cfeature.LAKES.with_scale('10m'),alpha=0.3,facecolor='xkcd:dusty blue')

# long > -141
station_cn=0
for sta in sta_list:
    if canada.contains(Point(sta.lon, sta.lat)):
        station_cn=station_cn+1
    # if sta.lat > 41.5 and sta.lon > -141:
        # ax1.scatter(sta.lon,sta.lat,marker='v', s=14, transform=ccrs.Geodetic(),c='none',edgecolors='rebeccapurple',alpha=.5,lw=.8)
print('Total stations in canada: ',station_cn)
# for i,lat in enumerate(lats):
#     if lat > 41.5 and long > -141:
#         ax1.plot(lons[i], lats[i], marker='^',markersize=8, linestyle='None',linewidth=.6, markerfacecolor='none', markeredgecolor='maroon', transform=ccrs.PlateCarree())

plt.show()

### plot Moho tiff
