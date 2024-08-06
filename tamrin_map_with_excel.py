import pandas as pd
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt


file = pd.read_excel("tamrin.xlsx")
x = file["Longitude"]
y = file["Latitude"]
p = file["Population"] / 1000
names = file["City"]


m = Basemap(
    llcrnrlon=44.0, llcrnrlat=25.0,
    urcrnrlon=63.0, urcrnrlat=40.0)
m.drawcoastlines()
m.drawcountries()


m.scatter(x, y, s=p, c="g", alpha=0.5)

plt.show()
plt.legend()