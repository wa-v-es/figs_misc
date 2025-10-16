from mpl_toolkits.basemap import Basemap
import numpy as np
import matplotlib.pyplot as plt
m = Basemap(width=3.e6,height=3.e6,\
            projection='gnom',lat_0=65.,lon_0=-155.,resolution='h',area_thresh=1000)
m.drawmapboundary(fill_color='white')
m.drawcountries(linewidth=0.55, linestyle='--', color='brown')
m.drawcoastlines(linewidth=.35)
m.fillcontinents(color='xkcd:fern',lake_color='xkcd:water blue', alpha=.5)
# labels = [left,right,top,bottom]
m.drawparallels(np.arange(10,90,5),linewidth=.40,zorder=50,color='navy',labels=[True,False,False,False])
m.drawmeridians(np.arange(-180,180,10),linewidth=.40,zorder=50,color='navy',labels=[False,False,False,True])

# plt.xlabel()
plt.title('Gnomonic AK')
plt.savefig('gonomonic_ak.png', dpi=350,bbox_inches='tight', pad_inches=0.1)

plt.show()
