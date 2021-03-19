import pandas as pd
from map_visualization import MapVisualization

with open("result.txt") as fp:
  lines = fp.readlines()

properties = []
for line in lines:
  properties.append(eval(line))

print(properties[0])

df = pd.DataFrame(properties)
print(df)

dublin_map = MapVisualization(df)
dublin_map.add_markers()
dublin_map.add_colorbar()
dublin_map.save("ireland_rent.html")
print("Done, please checkout the html file")
