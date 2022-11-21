import matplotlib.pyplot as plt
import numpy as np
import math

n1 = 1
n2 = 1.14
sdtDatang = np.arange(0, 90, 0.1)
teta1 = []
teta2 = []
y0 = []
x0 = np.arange(-5, 100, 1)
for i in range(len(x0)):
  y0.append(0)

def closestToNum(arr, K):
  return arr[min(range(len(arr)), key = lambda i: abs(arr[i] - K))]

for i in sdtDatang:
  teta1.append(math.radians(i))
  teta2.append(math.asin((n1/n2)*math.sin(math.radians(i))))

rTE = []
tTE = []
rTM = []
tTM = []

for i in range(len(teta1)):
  rTE.append(((n1*math.cos(teta1[i])) - (n2*math.cos(teta2[i]))) / ((n1*math.cos(teta1[i])) + (n2*math.cos(teta2[i]))))
  tTE.append((2*n1*math.cos(teta1[i]))/(n1*math.cos(teta1[i]) + n2*math.cos(teta2[i])))
  rTM.append((-(n1*math.cos(teta2[i])) + (n2*math.cos(teta1[i]))) / ((n1*math.cos(teta2[i])) + (n2*math.cos(teta1[i]))))
  tTM.append((2*n1*math.cos(teta1[i]))/(n1*math.cos(teta2[i]) + n2*math.cos(teta1[i])))

sdtBrewsterModeTM = 0
for i in range(len(rTM)):
  if(rTM[i] == closestToNum(rTM, 0)):
    sdtBrewsterModeTM = sdtDatang[i]

plt.plot(np.linspace(sdtBrewsterModeTM, sdtBrewsterModeTM), np.linspace(-1, 1), color='#32a68f', linestyle=':', label='Sudut Brewster pada mode TM \n(n2=%s)'%n2 + ': %s derajat'%sdtBrewsterModeTM)
plt.plot(np.arange(-5, 100, 1), np.linspace(0, 0, 105), '#000')
plt.plot(sdtDatang, rTE, label='rTE')
plt.plot(sdtDatang, tTE, label='tTE')
plt.plot(sdtDatang, rTM, 'r', label='rTM')
plt.plot(sdtDatang, tTM, 'g', label='tTM')
plt.xlabel('Sudut Datang')
plt.ylabel('t,r')
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.show()