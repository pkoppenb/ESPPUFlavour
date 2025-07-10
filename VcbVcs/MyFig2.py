# My attemps to re-implement Fig2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
plt.style.use('esppu.mplstyle')
fontNames = {'size'   : 15}   # Names of hadrons next to markers

# scan log from 0.001 to 2. -> -3 to log(2)/log(10.)
minE = 0.001
minE2 = 0.1
maxE = 3
maxE2 = 10
steps = 1000
log_syst = [ np.log(minE)+(x/steps)*(np.log(maxE)-np.log(minE)) for x in range(steps+1) ]
syst = [ np.exp(x) for x in log_syst ]

stat_Vcb = 0.15
stat_Vcs = 0.0085

fVcb = 0.5
fVcs = 0.35

Vcbunc = 1.15 # percent
Vcbdiscr = 5.5

Vcsunc = 100*0.006/0.975 # percent

# Marzocca assumes 3e8 W pairs
nFCC = 2*2.4e8          # 2.4 at 160. But there are more at higher energies.
nLC = 1.85e8            # from Jenny
nLEP3 = (5.6/19.2)*nFCC # These are scaled from FCC using xlsx table

# Ruan no longer used
Ruan = [ np.sqrt(0.72**2+0.20**2),
         np.sqrt(0.36**2+0.20**2),
         np.sqrt(0.95**2+0.20**2),
         np.sqrt(0.58**2+0.15**2),
         np.sqrt(0.34**2+0.18**2),
#         np.sqrt(1.5**2+0.20**2),
         np.sqrt(0.75**2+0.20**2),
        ]
RuanE = len(Ruan)*[ 0.8 ]# %

# doesn't work
my_err_Vcb = [ np.sqrt(stat_Vcb**2+(fVcb*x)**2) for x in syst ]
my_err_Vcs = [ np.sqrt(stat_Vcs**2+(fVcs*x)**2) for x in syst ]

def readFile(fn="Vcb_vs_syst.txt"):
    x = []
    y = []
    with open(fn,"r") as ff:
        for l in ff:
            ll = l.split()
            x.append(float(ll[0]))
            y.append(float(ll[1]))
    return x,y

def offsetStats(Vcb_in,ratio):
    """
    Offset to lower stats
    """
    # 1. first square it to get BFs.
    BF = [ v**2 for v in Vcb_in]
    
    statbase2 = BF[0]**2                         # statistics at 0 systematic
    syst2     = [ v**2 - statbase2 for v in BF ] # vector of systematics
    stat2     = statbase2/ratio                  # scale stats by ratio of lumis
    newBF     = [ np.sqrt(stat2+s2) for s2 in syst2 ] # new vector
    return [ np.sqrt(n) for n in newBF ]         # now get Vcb which is sqrt(bf)

    
Vcb_x, Vcb_FCC_y = readFile()
Vcs_x, Vcs_FCC_y = readFile("Vcs_vs_syst.txt")
print(Vcb_x, Vcb_FCC_y)

Vcb_LC_y = offsetStats(Vcb_FCC_y,nLC/nFCC)
Vcb_LEP3_y = offsetStats(Vcb_FCC_y,nLEP3/nFCC)
Vcs_LC_y = offsetStats(Vcs_FCC_y,nLC/nFCC)
Vcs_LEP3_y = offsetStats(Vcs_FCC_y,nLEP3/nFCC)
            
plt.figure(figsize=(7,5))
plt.rc('font', **fontNames)
fig, ax = plt.subplots()
fig.subplots_adjust(top=0.98,right=0.97,bottom=0.14,left=0.15)

############################################
# The Vcb Vcs plot
############################################

# plt.plot(syst,my_err_Vcs)
# plt.plot(syst,my_err_Vcb)
plt.plot(Vcb_x, Vcb_LEP3_y,label="$|V_{cb}|$, 5.6 ab$^{-1}$ at 230 GeV")
plt.plot(Vcb_x, Vcb_LC_y,label="$|V_{cb}|$, 8 ab$^{-1}$ at 550 GeV")
plt.plot(Vcb_x, Vcb_FCC_y,label="$|V_{cb}|$, 20 ab$^{-1}$ at 160 GeV")
plt.plot(Vcs_x, Vcs_LEP3_y,'--',label="$|V_{cs}|$, 5.6 ab$^{-1}$ at 230 GeV")
plt.plot(Vcs_x, Vcs_LC_y,'--',label="$|V_{cs}|$, 8 ab$^{-1}$ at 550 GeV")
plt.plot(Vcs_x, Vcs_FCC_y,'--',label="$|V_{cs}|$, 20 ab$^{-1}$ at 160 GeV")

plt.yscale('log')
plt.xscale('log')
plt.xlim([minE,maxE])
plt.ylim([0.005,2.0])
plt.legend()
plt.grid()
ax.set_yticks([0.01,0.05,0.1,0.5,1,2])
ax.get_yaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
ax.set_xticks([0.001,0.01,0.1,1])
ax.get_xaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())

"""
plt.text(0.3,0.01,"ESPP26, preliminary",
          fontsize=10.,
          bbox=dict(boxstyle="square",
                    ec=(33/256.,        83/256.,        172/256.),
                    fc=(217/256.,       237/256.,       237/256.))
          )
"""

plt.xlabel("Uncertainty on tagging efficiency [\%]")
plt.ylabel("Total uncertainty [\%]")
plt.savefig("VcbVcs.pdf",transparent=True)
plt.clf()

############################################
# The Vcb plot
############################################
fig, ax = plt.subplots()
fig.subplots_adjust(top=0.98,right=0.97,bottom=0.14,left=0.15)

plt.plot(Vcb_x, Vcb_LEP3_y,label="5.6 ab$^{-1}$ at 230 GeV")
plt.plot(Vcb_x, Vcb_LC_y,label="8 ab$^{-1}$ at 550 GeV")
plt.plot(Vcb_x, Vcb_FCC_y,label="20 ab$^{-1}$ at 160 GeV")

plt.xlim([minE2,maxE2])
plt.ylim([0.1,10.0])
plt.yscale('log')
plt.xscale('log')
plt.grid()
ax.set_yticks([0.1,0.2,0.5,1,2,5,10])
ax.get_yaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
ax.set_xticks([0.1,0.2,0.5,1,2,5])
ax.get_xaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())

plt.fill_between([minE2,maxE2], [0.1,0.1], [Vcbunc,Vcbunc], color='cyan', alpha=0.1, label='$|V_{cb}|^{\\rm excl}$ uncertainty')
plt.fill_between([minE2,maxE2], [Vcbunc,Vcbunc], [Vcbdiscr,Vcbdiscr], color='pink', alpha=0.3, label='$|V_{cb}|$ discrepancy')

# plt.scatter(RuanE,Ruan,20,marker='s',label='Liang et.al.',color='mediumturquoise')


plt.legend()
"""
plt.text(2.,7.,"ESPP26, preliminary",
          fontsize=10.,
          bbox=dict(boxstyle="square",
                    ec=(33/256.,        83/256.,        172/256.),
                    fc=(217/256.,       237/256.,       237/256.))
          )
"""

plt.xlabel("Uncertainty on tagging efficiency [\%]")
plt.ylabel("Total uncertainty on $|V_{cb}|$ [\%]")
plt.savefig("Vcb.pdf",transparent=True) 
plt.savefig("Vcb.png",transparent=True) 

############################################
# The Vcs plot
############################################
fig, ax = plt.subplots()
fig.subplots_adjust(top=0.98,right=0.97,bottom=0.14,left=0.15)

plt.plot(Vcs_x, Vcs_LEP3_y,label="5.6 ab$^{-1}$ at 230 GeV")
plt.plot(Vcs_x, Vcs_LC_y,label="8 ab$^{-1}$ at 550 GeV")
plt.plot(Vcs_x, Vcs_FCC_y,label="20 ab$^{-1}$ at 160 GeV")

plt.yscale('log')
plt.xscale('log')
plt.xlim([minE,maxE2])
plt.ylim([0.005,2.0])
plt.legend()
plt.grid()
ax.set_yticks([0.01,0.05,0.1,0.5,1,2])
ax.get_yaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
ax.set_xticks([0.001,0.01,0.1,1])
ax.get_xaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())

plt.fill_between([minE,maxE2], [0.005,0.005], [Vcsunc,Vcsunc], color='cyan', alpha=0.1, label='$|V_{cs}|$ uncertainty')

# plt.scatter(RuanE,Ruan,20,marker='s',label='Liang et.al.',color='mediumturquoise')


plt.legend()
"""
plt.text(2.,7.,"ESPP26, preliminary",
          fontsize=10.,
          bbox=dict(boxstyle="square",
                    ec=(33/256.,        83/256.,        172/256.),
                    fc=(217/256.,       237/256.,       237/256.))
          )
"""

plt.xlabel("Uncertainty on tagging efficiency [\%]")
plt.ylabel("Total uncertainty on $|V_{cs}|$ [\%]")
plt.savefig("Vcs.pdf",transparent=True) 
plt.savefig("Vcs.png",transparent=True) 
