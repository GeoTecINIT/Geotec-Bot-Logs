# Generates a txt file with the conversation
from datetime import datetime
from pprint import pprint
import numpy as np
import matplotlib.pyplot as plt
import f10013
n_id = 10013
data = f10013.data
dt = []
for d in data:
    line_id = d[0]
    user_c = d[1]
    bot_c = d[3]
    date = d[7]
    dt.append([line_id,datetime.strptime(date, "%Y-%m-%d %H:%M:%S" ),user_c,bot_c])

f = open("10013.txt","w") #print in document

f.write(str(n_id)), f.write("\n")
for i,t in enumerate(dt):
    si = i-1
    dts = dt[si][1]
    x = t[1] - dts
    f.write(str(t[0]))
    f.write(" - Total seconds: ")
    f.write(str(x.total_seconds()))
    f.write("\n User: ")
    f.write(str(t[2]))
    f.write("\n Bot: ")
    f.write(str(t[3]))
    f.write("\n")

f.close()
