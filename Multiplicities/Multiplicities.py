import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import sys
plt.style.use('/home/pkoppenb/cernbox/work/Future/ESPPU/Flavour/ESPPUFlavour/VcbVcs/esppu.mplstyle')
plt.rcParams['font.family'] = 'serif'

xs = 4
fig, ax = plt.subplots(figsize=(xs,xs))

microbarn = 1000
nanobarn = 1
labels = [ "LHC", "$\\Upsilon(4S)$", "$Z$" ]
bCross = [ 500*microbarn,                # 4pi
           1.05*nanobarn,                # babar book
           41.54*nanobarn*(15.12/69.91)  # lep1 book and PDG
]
bMult = [
    84,  # 2024 data
    10,  # hep-ex9907057.pdf
    23   # SLD
]
errs = [
    [50,0,0],
    [100,0,0]
    ]
for i in range(3): # need three series to get three colors
    plt.errorbar(bMult[i],bCross[i],xerr=[[errs[0][i]],[errs[1][i]]],fmt='o',label=labels[i])

plt.yscale('log')
plt.xscale('log')
# plt.ylim([0.2,2e6])
plt.xlim([7,120])
ax.set_xticks([10,20,30,50,100])
ax.get_xaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
plt.xlabel("Charged multiplicity in $b\\bar{b}$ events")
plt.ylabel("Cross-section $\\sigma(b\\bar{b})$ [nb]")
plt.legend()
plt.savefig("crossMult.pdf")
