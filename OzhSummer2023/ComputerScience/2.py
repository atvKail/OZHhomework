import math
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

bul = input("Округлять площадь? Yes/No >> ")
if bul == "yes": block = int(input("До скольки знаков после запятой? >> "))
(r, fi1, fi2) = map(int, input("Радиус, угол1 и угол2 >> ").split())

#calculate
alpha = abs(fi1 - fi2)
s = round(alpha * math.pi * pow(r, 2) / 360, block) if bul == "yes" else alpha * math.pi * pow(r, 2) / 360

#construction
c1 = plt.Circle ((0, 0), radius= r, color="r", fill=False)
x0 = np.arange(-r * 2, r * 2, r / 10)
x0sector = np.arange(0, r + r/20, r / 10)

(Xans, Yans) = ([], [])
(sL1x, sL1y) = ([], [])
(sL2x, sL2y) = ([], [])

for i in range(x0sector.size):
    sL1x.append(x0sector[i] * math.cos(fi1 * math.pi/180))
    sL1y.append(x0sector[i] * math.sin(fi1 * math.pi/180))
    sL2x.append(x0sector[i] * math.cos(fi2 * math.pi/180))
    sL2y.append(x0sector[i] * math.sin(fi2 * math.pi/180))

for i in range(x0.size):
    Xans.append(x0[i] * math.cos((alpha/2 + min(fi1, fi2)) * math.pi/180))
    Yans.append(x0[i] * math.sin((alpha/2 + min(fi1, fi2)) * math.pi/180))


#display
ax = plt.gca()
ax.add_artist(c1)

#ax.plot(x0, x0 * 0)
#ax.plot(x0 * 0, x0)

ax.plot(sL1x, sL1y)
ax.plot(sL2x, sL2y)

ax.plot(Xans, Yans)
plt.axis([-r * 2, r * 2, -r * 2, r * 2])
plt.text(Xans[len(Xans) * 2 // 3] + r / 10, Yans[len(Yans) * 2 // 3], f"S = {s}")
plt.axis("equal")
plt.show()