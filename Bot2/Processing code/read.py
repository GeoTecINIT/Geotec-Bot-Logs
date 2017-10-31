# Generates a plot with conversation timing
import json
from datetime import datetime
from pprint import pprint
import numpy as np
import matplotlib.pyplot as plt

with open('10001.json') as data_file:
    data = json.load(data_file)

#pprint(data[0]["time"])
dt = []
for d in data:
    line = d["time"]
    if "from" in d:
        user = d["from"]
    else:
        user = "user"
    date = line[0:line.find('.')]
    dt.append([user,datetime.strptime(date, "%Y-%m-%dT%H:%M:%S" )])
dif = []
difu = []
difn = []
difc = []
dift = 0.0
for i,t in enumerate(dt):
    si = i-1
    dts = dt[si][1]
    x = t[1] - dts
    if i > 0: #sacando el primero para que no se vuelva loco
        dif.append([t[0], x.total_seconds()])
        difu.extend(t[0][0:1])
        difn.append(x.total_seconds())
        dift = dift+x.total_seconds()
        if t[0] == "user":
            difc.append('r')
        else:
            difc.append('b')
difp = dift/(len(dt)-1)
print "Average = ", difp
print "Total time = ", dift
print "Conversations =", len(dt)

# draw the plot
ind = np.arange(len(difn))
width = 0.55
fig, ax = plt.subplots()
rects = ax.bar(ind, difn, width, color=difc)
ax.set_ylabel('Seconds')
ax.set_title('Seconds')
ax.set_xticks(ind+width)
ax.set_xticklabels(difu)
plt.show()
