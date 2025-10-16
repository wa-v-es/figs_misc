from mpl_toolkits.basemap import Basemap
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
mpl_version = tuple(map(int, mpl.__version__.split(".")))
axkwds = {"axisbg" if mpl_version < (2,) else "facecolor": "k"}

fig = plt.figure()
# global ortho map centered on lon_0,lat_0
lat_0=65.; lon_0=105.
# resolution = None means don't process the boundary datasets.
m1 = Basemap(projection='ortho',lon_0=lon_0,lat_0=lat_0,resolution=None)
# add an axes with a black background
ax = fig.add_axes([0.1,0.1,0.8,0.8], **axkwds)
# plot just upper right quadrant (corners determined from global map).
# keywords llcrnrx,llcrnry,urcrnrx,urcrnry used to define the lower
# left and upper right corners in map projection coordinates.
# llcrnrlat,llcrnrlon,urcrnrlon,urcrnrlat could be used to define
# lat/lon values of corners - but this won't work in cases such as this
# where one of the corners does not lie on the earth.
m = Basemap(projection='ortho',lon_0=lon_0,lat_0=lat_0,resolution='l',\
    llcrnrx=0.,llcrnry=0.,urcrnrx=m1.urcrnrx/2.,urcrnry=m1.urcrnry/2.)
m.drawmapboundary(fill_color='white')
m.drawcountries(linewidth=0.55, linestyle='--', color='brown')
m.drawcoastlines(linewidth=.35)
m.fillcontinents(color='xkcd:fern',lake_color='xkcd:water blue', alpha=.5)
# labels = [left,right,top,bottom]
m.drawparallels(np.arange(10,90,10),linewidth=.40,zorder=50,color='navy',labels=[True,False,False,False])
m.drawmeridians(np.arange(-180,180,20),linewidth=.40,zorder=50,color='navy',labels=[False,False,False,True])

# m.drawmapboundary()
plt.title('Quadrant Orthographic AK')
# plt.show()

plt.savefig('q_ortho_ak.png', dpi=350,bbox_inches='tight', pad_inches=0.1)

# plt.show()
