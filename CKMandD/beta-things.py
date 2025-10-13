
# coding: utf-8

# In[ ]:


import matplotlib
import matplotlib.pyplot as plt
import numpy as np
plt.style.use('esppu.mplstyle')
plt.rcParams['font.family'] = 'serif'


# In[ ]:


def makeplot(title,
             lhcb_d=None, lhcb_p=None,
             belle2_d=None, belle2_p=None,
             fcc_d=None, fcc_p=None,
             theo=None,
             savename=None, 
             wantlog=True,
             ylim = None,
             legend=True,
            wantdeg = False): 
    
    import matplotlib.pyplot as plt

    fig, ax = plt.subplots(figsize=(1.25*2.5, 1.25*2))
    #ax.spines["right"].set_visible(False)

    if lhcb_d is not None and lhcb_p is not None:
        ax.plot(lhcb_d, 1e0 * lhcb_p, "o", label="LHC", color="C0")

    if fcc_d is not None and fcc_p is not None:
        ax.plot(fcc_d, 1e0 * fcc_p, "o", label="FCC-ee", color="C1")
        ax.plot(fcc_d, np.sqrt(6/1.4) * fcc_p, "o", label="LEP3", color="C4")

    if belle2_d is not None and belle2_p is not None:
        ax.plot(belle2_d, 1e0 * belle2_p, "o", label="Belle II", color="C2")

    if theo is not None:
        ax.axhline(theo, ls="--", label="SM")

    # Add "ESPP26 preliminary" in top right, small font
    #ax.text(0.98, 0.98, "ESPP26\npreliminary",
    #        ha="right", va="top", fontsize=8, transform=ax.transAxes)

    # Title and axes
    #ax.set_title(title)
    plt.ylabel(title)
    ax.set_xticks([0, 1, 2, 3])
    ax.set_xticklabels([r"$\mathrm{today}$", r"$2030\mathrm{s}$", r"$2040\mathrm{s}$", r"$2050\mathrm{s}$"])

    if wantlog:
        ax.set_yscale("log")
    
    if ylim is not None: plt.ylim(ylim)
    plt.xlim(-0.3, 3.3)
    
    fig.tight_layout()

    ax.legend(loc="upper right", frameon=True, ncol=1,
             fontsize=10, labelspacing=0.25 )

    '''
    if wantdeg:
        def mrad_to_deg(mrad):
            return mrad * (180 / (np.pi * 1000))  # 1 mrad = 0.0572958 deg

        def deg_to_mrad(deg):
            return deg * (np.pi * 1000 / 180)

        # Add secondary y-axis with degree scale
        ax_deg = ax.secondary_yaxis('right', functions=(mrad_to_deg, deg_to_mrad))
        ax_deg.set_ylabel('$[^{\circ}]$')
    '''
    
    # Save legend as a separate plot
    """
    if legend:
        handles, labels = ax.get_legend_handles_labels()
        if handles:  # Only make legend plot if something to show
            fig_leg, leg_ax = plt.subplots(figsize=(2.5, 0.6))
            leg_ax.axis("off")
            leg_ax.legend(handles, labels, loc="center", frameon=False, ncol=2)
            fig_leg.tight_layout()
            if savename:
                fig_leg.savefig(savename.replace(".pdf", "_legend.pdf"))
    """

    if savename:
        fig.savefig(savename)


# def makeplot(title,
#              lhcb_d=None, lhcb_p=None,
#              belle2_d=None, belle2_p=None,
#              fcc_d=None, fcc_p=None,
#              theo=None,
#              savename=None, 
#             wantlog=True,
#             legend=True): 
#     plt.figure(figsize=(2.5,3))
#     
#     if lhcb_d is not None and lhcb_p is not None:
#         plt.plot(lhcb_d, 1e0*lhcb_p, "o", label="LHC", color="C0")
# 
#     if fcc_d is not None and fcc_p is not None:
#         plt.plot(fcc_d, 1e0*fcc_p, "o", label="", color="C1")
# 
#     if belle2_d is not None and belle2_p is not None:
#         plt.plot(belle2_d, 1e0*belle2_p, "o", label="Belle II", color="C2")
#     
#     if theo is not None:
#         plt.axhline(theo, ls="--", label="SM")
#      
#     if legend: plt.legend()
#     #plt.xlabel("year")
#     plt.title(title)# $[10^{-5}]$")
#     
#     
#     
#     plt.xticks(ticks=[0, 1, 2, 3], labels=["today", "2030s", "2040s", "2050s"])
#     
#     if wantlog: plt.semilogy()
#     plt.tight_layout()
#     
#     if savename is not None: plt.savefig(savename)
# 
# 

# In[ ]:


import numpy as np
import matplotlib.pyplot as plt

from matplotlib.lines import Line2D
from matplotlib.patches import Patch

def makeplot_withrange(title,
                       fcc_lo, fcc_up,
                       fcc_d,
                       lhcb_d=None, lhcb_p=None,
                       belle2_d=None, belle2_p=None,
                       theo=None,
                       savename=None, 
                       wantlog=True,
                       legend=True): 

    fig, ax = plt.subplots(figsize=(2.5, 3))
    legend_elements = []

    if lhcb_d is not None and lhcb_p is not None:
        ax.plot(lhcb_d, 1e0 * lhcb_p, "o", color="C0")
        legend_elements.append(Line2D([0], [0], marker="o", linestyle="None", color="C0", label="LHC"))

    # FCC ranges
    fcc_x = [fcc_d - 0.0, fcc_d + 0.2]
    fcc_y1 = [fcc_lo, fcc_lo]
    fcc_y2 = [fcc_up, fcc_up]

    s = np.sqrt(6 / 2)
    fcc_xb = [fcc_d - 0.2, fcc_d + 0.0]
    fcc_y1b = [s * fcc_lo, s * fcc_lo]
    fcc_y2b = [s * fcc_up, s * fcc_up]

    ax.fill_between(fcc_xb, fcc_y1b, fcc_y2b, alpha=0.5, color="C4")
    legend_elements.append(Patch(facecolor="C4", alpha=0.5, label=r"LEP3"))

    ax.fill_between(fcc_x, fcc_y1, fcc_y2, alpha=0.5, color="C1")
    legend_elements.append(Patch(facecolor="C1", alpha=0.5, label=r"FCC-ee"))

    if belle2_d is not None and belle2_p is not None:
        ax.plot(belle2_d, 1e0 * belle2_p, "o", color="C2")
        legend_elements.append(Line2D([0], [0], marker="o", linestyle="None", color="C2", label="Belle II"))

    if theo is not None:
        ax.axhline(theo, ls="--", color="black")
        legend_elements.append(Line2D([0], [0], linestyle="--", color="black", label="SM"))

    # ESPP26 label
    #ax.text(0.98, 0.98, "ESPP26\npreliminary",
    #        ha="right", va="top", fontsize=8, transform=ax.transAxes)

    ax.set_title(title)
    ax.set_xticks([0, 1, 2, 3])
    ax.set_xticklabels([r"$\mathrm{today}$", "$2030s$", "$2040s$", "$2050s$"])

    if wantlog:
        ax.set_yscale("log")

    fig.tight_layout()

    ax.legend(handles=legend_elements, loc="center", frameon=False, ncol=2,
                  fontsize=11, labelspacing=0.3 )
    fig_leg.tight_layout()

    '''
    if legend and legend_elements:
        fig_leg, leg_ax = plt.subplots(figsize=(2.5, 0.6))
        leg_ax.axis("off")
        leg_ax.legend(handles=legend_elements, loc="center", frameon=False, ncol=2)
        fig_leg.tight_layout()
        if savename:
            fig_leg.savefig(savename.replace(".pdf", "_legend.pdf"))
    '''
    
    if savename:
        fig.savefig(savename)


# def makeplot_withrange(title,
#                        fcc_lo, fcc_up,
#                          fcc_d,
#                          lhcb_d=None, lhcb_p=None,
#                          belle2_d=None, belle2_p=None,
#                          theo=None,
#                          savename=None, 
#                         wantlog=True,
#                         legend=True): 
#     #fig, ax = plt.figure(figsize=(2.5,3))
#     fig, ax = plt.subplots(figsize=(2.5, 3))
#     
#     if lhcb_d is not None and lhcb_p is not None:
#         plt.plot(lhcb_d, 1e0*lhcb_p, "o", label="LHC", color="C0")
# 
#     fcc_x = [fcc_d-0., fcc_d+0.2]
#     fcc_y1 = [fcc_lo, fcc_lo]
#     fcc_y2 = [fcc_up, fcc_up]
# 
#     s = np.sqrt(6/2)
#     fcc_xb = [fcc_d-0.2, fcc_d+0.]
#     fcc_y1b = [s*fcc_lo, s*fcc_lo]
#     fcc_y2b = [s*fcc_up, s*fcc_up]
# 
#     plt.fill_between(fcc_xb, fcc_y1b, fcc_y2b, alpha=0.5, color="C4", 
#                      label="$2\\times10^{12}\,{\\rm Z}^0$")
#     plt.fill_between(fcc_x, fcc_y1, fcc_y2, alpha=0.5, color="C1", 
#                      label="$6\\times10^{12}\,{\\rm Z}^0$")
# 
#     if belle2_d is not None and belle2_p is not None:
#         plt.plot(belle2_d, 1e0*belle2_p, "o", label="Belle II", color="C2")
#     
#     if theo is not None:
#         plt.axhline(theo, ls="--", label="SM")
#      
#     if legend: plt.legend()
#     #plt.xlabel("year")
#     plt.title(title)# $[10^{-5}]$")
#     
#     plt.xticks(ticks=[0, 1, 2, 3], labels=["today", "2030s", "2040s", "2050s"])
#     
#     if wantlog: plt.semilogy()
#     plt.tight_layout()
# 
#     # Add "ESPP26 preliminary" in top right, small font
#     ax.text(0.98, 0.98, "ESPP26\npreliminary",
#             ha="right", va="top", fontsize=8, transform=ax.transAxes)
#     
#     if savename is not None: plt.savefig(savename)

# ## sin2beta

# In[ ]:


belle2_p = np.array([1.2, 0.4, 0.3])
belle2_d = np.array([0, 1, 2])

lhcb_d = np.array([0, 1, 2])
lhcb_p = np.array([0.57, 0.2, 0.08])

fcc_d = np.array([3])
fcc_p = np.array([0.18])

theo=0.15


# In[ ]:


makeplot("$\sigma(\\beta)$ $[^{\circ}]$",
        lhcb_d = lhcb_d, lhcb_p=lhcb_p,
        belle2_d = belle2_d, belle2_p = belle2_p, 
        fcc_d = fcc_d, fcc_p = fcc_p,
        savename="figures/sin2beta.pdf",
        theo=theo)


# ## phi_s

# In[ ]:


lhcb_d = np.array([0, 1, 2])
lhcb_p = np.array([20, 8, 3])

fcc_d = np.array([3])
fcc_p = np.array([2])

theo=1.92


# In[ ]:


makeplot("$\sigma(\phi_s)$ [mrad]",
        lhcb_d = lhcb_d, lhcb_p=lhcb_p,
        fcc_d = fcc_d, fcc_p = fcc_p,
        savename="figures//phis.pdf",
        theo=theo,
        ylim=(8e-1, 30),
        wantdeg=True)


# ## phi_s in Bs -> phi phi

# In[ ]:


lhcb_d = np.array([0, 1, 2])
lhcb_p = np.array([69, 22, 9])

fcc_d = np.array([3])
fcc_p = np.array([9])

theo=1


# In[ ]:


makeplot("$\sigma(\phi_s(B_s^0\\to\phi\phi))$ [mrad]",
        lhcb_d = lhcb_d, lhcb_p=lhcb_p,
        fcc_d = fcc_d, fcc_p = fcc_p,
        savename="figures//phis_bsphihi.pdf",
        ylim=(0.8, 90),
        theo=theo)


# ## alpha

# In[ ]:


belle2_p = np.array([6.6, 2.5, 0.6])
belle2_d = np.array([0, 1, 2])

fcc_lo = 0.1
fcc_up = 0.25
fcc_d = 3

theo=1.


# In[ ]:


makeplot_withrange("$\sigma(\\alpha)$ $[^{\circ}]$",
                    fcc_lo = fcc_lo, 
                   fcc_up=fcc_up,
                     fcc_d=fcc_d,
                     belle2_d=belle2_d, belle2_p=belle2_p,
                     theo=theo,
                     savename="figures//alpha.pdf", 
                    wantlog=True,
                    legend=True)

