# Generates a plot with conversation timing but only with the bot response
import json
from datetime import datetime
from pprint import pprint
import numpy as np
import matplotlib.pyplot as plt
n_id = 10002
with open('f10002.json') as data_file:
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
    c_id = user = d["_id"]
    dt.append([user,datetime.strptime(date, "%Y-%m-%dT%H:%M:%S" ), c_id])
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
        if t[0] != "user":
            difc.append('b')
            dif.append([t[0], x.total_seconds()])
            difu.extend(t[2][-3:])
            difn.append(x.total_seconds())
            dift = dift+x.total_seconds()
difp = dift/(len(dt)-1)
print "Average= ", difp
print "Total= ", dift
print "Conversations =", len(difn)

f = open("totals.py","a") #print in document
f.write("[")
f.write(str(n_id))
f.write(",")
f.write(str(difp))
f.write(",")
f.write(str(dift))
f.write(",")
f.write(str(len(dt)))
f.write("],\n")
f.close()

# draw the plot
ind = np.arange(len(difn))
width = 0.55
fig, ax = plt.subplots()
rects = ax.bar(ind, difn, width, color=difc)
ax.set_ylabel('Seconds')
ax.set_title('Seconds')
ax.set_xticks(ind+width)
ax.set_xticklabels(difu)
# plt.show()
plt.savefig('10002.png', dpi=300)
