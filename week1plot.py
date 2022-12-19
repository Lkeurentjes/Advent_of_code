plot = ["127 11th St SE, Washington DC 20002",
        "1309D Washington DC 20002",
          "1207 D St NE Washington DC 20002",
        "1216 Holbrook St NE Washington DC 20002",
        "1812 D St NE Washington DC 20002",
          "1718 D St NE Washington DC 20002",
        "1833 S Capitol St SE Washington DC 20010",
          "37 16th St NE Washington DC 20002",
        "32 16th St SE Washington DC 20003",
        "19 14th St SE Washington DC 20003",
          "99 14th St NE Washington DC 20002"]

import pandas as pd
import io
from geopy.geocoders import Nominatim
import matplotlib.pyplot as plt
from matplotlib.path import Path
import matplotlib.patches as patches

geolocator = Nominatim(user_agent="test")

lat = []
lon = []
vertices =[]
for d in plot:
    print(d)
    data =geolocator.geocode(d)
    print(data)
    if data is not None:
        print(data.raw.get("lat"), data.raw.get("lon"))
        lat.append(data.raw.get("lat"))
        lon.append(data.raw.get("lon"))
        vertices.append((data.raw.get("lat"), data.raw.get("lon")))
    print("\n")

vertices.append(vertices[0])
codes = [
    Path.MOVETO,
    Path.LINETO,
    Path.LINETO,
    Path.LINETO,
    Path.LINETO,
    Path.LINETO,
    Path.LINETO,
    Path.LINETO,
    Path.LINETO,
    Path.LINETO,
    Path.LINETO,
    # Path.LINETO,
    # Path.LINETO,
    Path.CLOSEPOLY,
]
print(vertices,"\n",codes)
path = Path(vertices, codes)

fig, ax = plt.subplots()
patch = patches.PathPatch(path, facecolor='orange', lw=2)
ax.add_patch(patch)
ax.set_xlim(38.88, 38.91 )
ax.set_ylim(-76.97, -77.07)

# plt.plot(lat, lon, "ro")
# n = ["A","B","C","D","E","F","G","H","I","J","K"]
# for i, txt in enumerate(n):
#     ax.annotate(txt,(lat[i], lon[i]))

# plt.axis('equal')
plt.show()
