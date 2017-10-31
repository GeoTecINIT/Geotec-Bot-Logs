# Generates a plot with conversation timing
import json
from datetime import datetime
from pprint import pprint
import numpy as np
import matplotlib.pyplot as plt
n_id = 10013
with open('f10013.json') as data_file:
    data = json.load(data_file)

#pprint(data[0]["time"])
dt = []
for d in data:
    line = d["time"]
    m = d["message"]
    c_id = d["_id"]
    if "from" in d:
        user = d["from"]
    else:
        user = "user"
    date = line[0:line.find('.')]
    dt.append([user,datetime.strptime(date, "%Y-%m-%dT%H:%M:%S" ),m,c_id])

f = open("10013.txt","w") #print in document

f.write(str(n_id)), f.write("\n")
for i,t in enumerate(dt):
    si = i-1
    dts = dt[si][1]
    x = t[1] - dts
    f.write(str(t[3][-4:]))
    f.write(" - Total seconds: ")
    f.write(str(x.total_seconds()))
    f.write(" ")
    f.write(str(t[0]))
    f.write(": ")
    f.write(t[2].encode('utf-8'))
    f.write("\n")

f.close()

