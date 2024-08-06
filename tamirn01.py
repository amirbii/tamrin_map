import numpy as np
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt

m = Basemap(
    llcrnrlon=44.0, llcrnrlat=25.0,
    urcrnrlon=63.0, urcrnrlat=40.0)
m.drawcoastlines()
m.drawcountries()

x = [51.389, 59.6168, 51.666, 50.9391, 52.5837, 46.2919, 50.8759, 48.6691, 47.065, 45.0761]
y = [35.6892, 36.2605, 32.6539, 35.84, 29.5918, 38.0848, 34.6399, 31.3183, 34.3142, 37.5527]
p = [9039000, 3057000, 2076000, 1992000, 1869000, 1561000, 1345000, 1303000, 946000, 736000]
p1 = np.array(p) / 1000
m.scatter(x, y, s=p1, c="g", alpha=0.5)

plt.show()
plt.legend()
