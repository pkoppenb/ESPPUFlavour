
# coding: utf-8

# In[ ]:


import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.lines import Line2D
from matplotlib.patches import Patch
plt.style.use('esppu.mplstyle')
plt.rcParams['font.family'] = 'serif'


# In[ ]:


#0: today, 1: 30s, 2: 40s, 3: 50s

belle2_p = np.array([40e-4, 9.5e-4, 6.2e-4])
belle2_d = np.array([0, 1, 2])

lhcb_d = np.array([0, 1, 2])
lhcb_p = np.array([36e-4, 5e-4, 2e-4])

fcc_d = np.array([3., 3.2])
fcc_up = np.sqrt(5/6)*np.array([0.25e-4, 0.25e-4])
fcc_lo = np.sqrt(5/6)*np.array([2e-4, 2e-4])

lep_d = np.array([3.-0.2, 3.])
lep_up = np.sqrt(5/1.4)*np.array([0.25e-4, 0.25e-4])
lep_lo = np.sqrt(5/1.4)*np.array([2e-4, 2e-4])

theo = 0.5e-4


# In[ ]:


fig = plt.figure(figsize=(1.25*2.5,1.25*2))
ax = plt.gca()


handles = []
labels = []

l1, = plt.plot(lhcb_d, 1e0*lhcb_p, "o", label="LHC", color="C0")
handles.append(l1)
labels.append("LHCb")

l3, = plt.plot(belle2_d, 1e0*belle2_p, "o", label="Belle II", color="C2")
handles.append(l3)
labels.append("Belle II")

#l2, = plt.plot(fcc_d, 1e0*fcc_p, "o", label="FCC-ee ($6\\times10^{12}\,{\\rm Z}^0$)", color="C1")
l2 = plt.fill_between(fcc_d, fcc_lo, fcc_up, alpha=0.5, color="C1", label="FCC")
handles.append(l2)
labels.append("$6\\times10^{12}\,{\\rm Z}^0$")


#l4, = plt.plot(lep_d, 1e0*lep_p, "o", label="LEP3 ($2\\times10^{12}\,{\\rm Z}^0$)", color="C4")
l4 = plt.fill_between(lep_d, lep_lo, lep_up, alpha=0.5, color="C4", label="FCC")

handles.append(l4)
labels.append("LEP3 ($2\\times10^{12}\,{\\rm Z}^0$)")

'''
# Add small text at top-right *inside the plot area*
ax.text(0.98, 0.98, "ESPP26\npreliminary",
        transform=ax.transAxes,  # axes coordinates
        ha='right', va='top',
        fontsize=8,              # smaller font
        bbox=dict(facecolor='white', edgecolor='none', alpha=0.8, pad=2))
'''

plt.axhline(theo, ls="--", label="SM")



#plt.legend()
#plt.xlabel("year")
plt.ylabel("$\sigma(a^{sl}_d)$")# $[10^{-5}]$")



plt.xticks(ticks=[0, 1, 2, 3], labels=["today", "2030s", "2040s", "2050s"])

plt.semilogy()
plt.tight_layout()


"""
fig_legend = plt.figure()
# Add the legend to the new figure
# You can adjust parameters like loc and fontsize
fig_legend.legend(handles=handles, labels=labels, loc='center', fontsize=12)

# Optional: turn off axes in the legend-only figure
fig_legend.gca().axis('off')
"""

handles = [
    Line2D([], [], marker='o', color='C0', linestyle='None', label='LHCb'),
    Line2D([], [], marker='o', color='C2', linestyle='None', label='Belle II'),
    Patch(facecolor='C1', alpha=0.5, label='FCC-ee'),
    Patch(facecolor='C4', alpha=0.5, label='LEP3'),
    Line2D([], [], marker='None', color='C0', linestyle='--', label='SM')
]
labels = [h.get_label() for h in handles]

plt.ylim(1.5e-5, 14e-3)

plt.legend(handles=handles, labels=labels, loc='lower left', 
          fontsize=10, labelspacing=0.25)

plt.savefig("figures/asld-projections.pdf")


#fig_legend = plt.figure()
# Add the legend to the new figure
# You can adjust parameters like loc and fontsize
#fig_legend.legend(handles=handles, labels=labels, loc='upper right', fontsize=12)

# Optional: turn off axes in the legend-only figure
#fig_legend.gca().axis('off')

# Show both figures

plt.show()



# ## now a_sl^s

# In[ ]:


#belle2_p = np.array([40e-4, 9.5e-4, 6.2e-4])
#belle2_d = np.array([0, 1, 2])

lhcb_d = np.array([0, 1, 2])
lhcb_p = np.array([33e-4, 7e-4, 3e-4])

"""
fcc_d = np.array([3])
fcc_p = np.array([np.sqrt(6/5)*0.25e-4])

lep_d = np.array([3])
lep_p = np.array([np.sqrt(2/5)*0.25e-4])
"""

fcc_d = np.array([3., 3.2])
fcc_up = np.sqrt(5/6)*np.array([0.25e-4, 0.25e-4])
fcc_lo = np.sqrt(5/6)*np.array([2e-4, 2e-4])

lep_d = np.array([3.-0.2, 3.])
lep_up = np.sqrt(5/1.4)*np.array([0.25e-4, 0.25e-4])
lep_lo = np.sqrt(5/1.4)*np.array([2e-4, 2e-4])

theo = 0.2e-5


# In[ ]:


fig = plt.figure(figsize=(1.25*2.5,1.25*2))

ax = plt.gca()


handles = []
labels = []

l1, = plt.plot(lhcb_d, 1e0*lhcb_p, "o", label="LHC", color="C0")
handles.append(l1)
labels.append("LHCb")

#l3, = plt.plot(belle2_d, 1e0*belle2_p, "o", label="Belle II", color="C2")
#handles.append(l3)
#labels.append("Belle II")

#l2, = plt.plot(fcc_d, 1e0*fcc_p, "o", label="FCC-ee ($6\\times10^{12}\,{\\rm Z}^0$)", color="C1")
l2 = plt.fill_between(fcc_d, fcc_lo, fcc_up, alpha=0.5, color="C1", label="FCC")
handles.append(l2)
labels.append("$6\\times10^{12}\,{\\rm Z}^0$")


#l4, = plt.plot(lep_d, 1e0*lep_p, "o", label="LEP3 ($2\\times10^{12}\,{\\rm Z}^0$)", color="C4")
l4 = plt.fill_between(lep_d, lep_lo, lep_up, alpha=0.5, color="C4", label="FCC")

handles.append(l4)
labels.append("LEP3 ($2\\times10^{12}\,{\\rm Z}^0$)")

# Add small text at top-right *inside the plot area*
'''
ax.text(0.98, 0.98, "ESPP26\npreliminary",
        transform=ax.transAxes,  # axes coordinates
        ha='right', va='top',
        fontsize=8,              # smaller font
        bbox=dict(facecolor='white', edgecolor='none', alpha=0.8, pad=2))
'''

plt.axhline(theo, ls="--", label="SM")



#plt.legend()
#plt.xlabel("year")
plt.ylabel("$\sigma(a^{sl}_s)$")# $[10^{-5}]$")



plt.xticks(ticks=[0, 1, 2, 3], labels=["today", "2030s", "2040s", "2050s"])

plt.semilogy()
plt.tight_layout()


"""
fig_legend = plt.figure()
# Add the legend to the new figure
# You can adjust parameters like loc and fontsize
fig_legend.legend(handles=handles, labels=labels, loc='center', fontsize=12)

# Optional: turn off axes in the legend-only figure
fig_legend.gca().axis('off')
"""

handles = [
    Line2D([], [], marker='o', color='C0', linestyle='None', label='LHCb'),
    #Line2D([], [], marker='o', color='C2', linestyle='None', label='Belle II'),
    Patch(facecolor='C1', alpha=0.5, label='FCC-ee'),
    Patch(facecolor='C4', alpha=0.5, label='LEP3'),
    Line2D([], [], marker='None', color='C0', linestyle='--', label='SM')

]
labels = [h.get_label() for h in handles]

plt.legend(handles=handles, labels=labels, loc='center left', 
           bbox_to_anchor=(0.05, 0.3),
          fontsize=10, labelspacing=0.25)

plt.ylim(1e-6, 40e-3)
plt.savefig("figures/asls-projections.pdf")


'''
fig_legend = plt.figure()
# Add the legend to the new figure
# You can adjust parameters like loc and fontsize
fig_legend.legend(handles=handles, labels=labels, loc='center', fontsize=12)

# Optional: turn off axes in the legend-only figure
fig_legend.gca().axis('off')

# Show both figures
'''

plt.show()


# In[ ]:


plt.figure(figsize=(3,3))

#plt.plot(lhcb_d, 1e0*lhcb_p, "o", label="LHC")
#plt.plot(fcc_d, 1e0*fcc_p, "o", label="FCC-ee")
#plt.plot(belle2_d, 1e0*belle2_p, "o", label="Belle II")


plt.plot(lhcb_d, 1e0*lhcb_p, "o", label="LHC", color="C0")
plt.plot(fcc_d, 1e0*fcc_p, "o", label="FCC-ee ($6\\times10^{12}\,{\\rm Z}^0$)", color="C1")
plt.plot(belle2_d, 1e0*belle2_p, "o", label="Belle II", color="C2")
plt.plot(lep_d, 1e0*lep_p, "o", label="LEP3 ($2\\times10^{12}\,{\\rm Z}^0$)", color="C4")

plt.axhline(theo, ls="--", label="SM")



plt.legend()
plt.xlabel("year")
plt.ylabel("$\sigma(a^{sl}_s)$")# $[10^{-5}]$")



plt.xticks(ticks=[0, 1, 2, 3], labels=["today", "2030s", "2040s", "2050s"])

plt.semilogy()
plt.tight_layout()

plt.savefig("/Users/robert/Downloads/asls-projections.pdf")

