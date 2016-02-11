import pandas
import numpy as np
import math
import matplotlib.pyplot as plt


laser_data = pandas.read_csv("laser.csv")

time = range(len(laser_data))

laser_range_data = pandas.Series(laser_data["range"], index=time)

laser_range_data.plot(title='How data looks')


def changedetect(d):
    n = len(d)
    # dbar = sum(d)/float(n)
    dbar = np.mean(d)

    # dsbar = sum (d*d)/float(n)
    dsbar = np.mean(np.multiply(d,d))

    fac = dsbar-np.square(dbar)

    summ = 0
    summup = []

    for z in range(n):
        summ+=d[z]
        summup.append(summ)

    y = []

    for m in range(n-1):
        pos=m+1
        mscale = 4*(pos)*(n-pos)
        Q = summup[m]-(summ-summup[m])
        U = -np.square(dbar*(n-2*pos) + Q)/float(mscale) + fac
        y.append(-(n/float(2)-1)*math.log(n*U/2) - 0.5*math.log((pos*(n-pos))))

    z, zz = np.max(y), np.argmax(y)

    mean1 = sum(d[:zz+1])/float(len(d[:zz+1]))
    mean2=sum(d[(zz+1):n])/float(n-1-zz)

    return y, zz, mean1, mean2


step_like = changedetect(laser_range_data)
#print(step_like)
step_series = pandas.Series(step_like[0],index=time[1:])

plt.figure()


step_series.plot(title='Log likelihood of step change location in laser range data')

plt.show()
