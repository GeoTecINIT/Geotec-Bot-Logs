# Generates a plot with conversation timing with bot responses
from datetime import datetime
from pprint import pprint
import numpy as np
import matplotlib.pyplot as plt
import f10010
n_id = 10010
data = f10010.data
dt = []
for d in data:
    line_id = d[0]
    date = d[7]
    dt.append([line_id,datetime.strptime(date, "%Y-%m-%d %H:%M:%S" )])
dif = []
difu = []
difn = []
dift = 0.0
for i,t in enumerate(dt):
    si = i-1
    dts = dt[si][1]
    x = t[1] - dts
    if i > 0: #sacando el primero para que no se vuelva loco
        dif.append([t[0], x.total_seconds()])
        difu.append(t[0])
        difn.append(x.total_seconds())
        dift = dift+x.total_seconds()

difp = dift/(len(dt)-1)
print "Average= ", difp
print "Total= ", dift
print "Conversations =", len(dt)
f = open("totals.py","a") #print in document
f.write("[")
f.write(str(n_id))
f.write(",")
f.write(str(difp))
f.write(",")
f.write(str(dift))
f.write(",")
f.write(str(len(dt)))
f.write("]\n")
f.close()

# draw the plot
ind = np.arange(len(difn))
width = 0.55
fig, ax = plt.subplots()
rects = ax.bar(ind, difn, width, color="r")
ax.set_ylabel('Seconds')
ax.set_title('Seconds')
ax.set_xticks(ind+width)
ax.set_xticklabels(difu)
# plt.show()
plt.savefig('10010.png')
