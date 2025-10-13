
# coding: utf-8

# In[ ]:


import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.lines import Line2D
from matplotlib.legend_handler import HandlerTuple
from iminuit import Minuit


# In[ ]:


plt.style.use('esppu.mplstyle')
plt.rcParams['font.family'] = 'serif'


# ## define all functions for observables

# ### xcp, dx, ycp, dy for B0-> KS pi pi

# In[ ]:


def xcp(x, y, qp, phi):
    ret = x*np.cos(phi)*(qp+1/qp)
    ret += y*np.sin(phi)*(qp-1/qp)
    return 0.5*ret


# In[ ]:


def dx(x, y, qp, phi):
    ret = x*np.cos(phi)*(qp-1/qp)
    ret += y*np.sin(phi)*(qp+1/qp)
    return 0.5*ret


# In[ ]:


def ycp(x, y, qp, phi):
    ret = y*np.cos(phi)*(qp+1/qp)
    ret -= x*np.sin(phi)*(qp-1/qp)
    return 0.5*ret


# In[ ]:


def dy(x, y, qp, phi):
    ret = y*np.cos(phi)*(qp-1/qp)
    ret -= x*np.sin(phi)*(qp+1/qp)
    return 0.5*ret


# ### AGamma for D0-> hh

# In[ ]:


def agamma(x, y, qp, phi):
    ret = y*np.cos(phi)*(qp-1/qp)
    ret -= x*np.sin(phi)*(qp+1/qp)
    return 0.5*ret


# ### xpp2 (x prime plus square), xpm2, ypp, ypm

# In[ ]:


def xp(x, y, delta):
    return x*np.cos(delta)+y*np.sin(delta)

def yp(x, y, delta):
    return y*np.cos(delta)-x*np.sin(delta)


# In[ ]:


def xpp2(x,y, qp, phi, delta):
    myxp = xp(x,y,delta)
    myyp = yp(x,y,delta)

    ret = qp*(myxp*np.cos(phi)+myyp*np.sin(phi))
    return ret*ret


# In[ ]:


def xpm2(x,y, qp, phi, delta):
    myxp = xp(x,y,delta)
    myyp = yp(x,y,delta)

    ret = (1/qp)*(myxp*np.cos(phi)-myyp*np.sin(phi))
    return ret*ret


# In[ ]:


def ypp(x,y, qp, phi, delta):
    myxp = xp(x,y,delta)
    myyp = yp(x,y,delta)

    ret = qp*(myyp*np.cos(phi)-myxp*np.sin(phi))
    return ret


# In[ ]:


def ypm(x,y, qp, phi, delta):
    myxp = xp(x,y,delta)
    myyp = yp(x,y,delta)

    ret = (1/qp)*(myyp*np.cos(phi)+myxp*np.sin(phi))
    return ret


# ## define central values for all parameters

# In[ ]:


x_val = 0.00407
y_val = 0.00645
qp_val = 1.
phi_val = 0. 

delta_val = np.deg2rad(11.4)


# In[ ]:


xcp_val = xcp(x=x_val, y=y_val, qp=qp_val, phi=phi_val)
ycp_val = ycp(x=x_val, y=y_val, qp=qp_val, phi=phi_val) #0.00551
dx_val = dx(x=x_val, y=y_val, qp=qp_val, phi=phi_val) #-0.00029
dy_val = dy(x=x_val, y=y_val, qp=qp_val, phi=phi_val) #0.00031

agamma_val = agamma(x=x_val, y=y_val, qp=qp_val, phi=phi_val) #0.000089

xpp2_val = xpp2(x=x_val, y=y_val, qp=qp_val, phi=phi_val, delta=delta_val)
xpm2_val = xpm2(x=x_val, y=y_val, qp=qp_val, phi=phi_val, delta=delta_val)
ypp_val = ypp(x=x_val, y=y_val, qp=qp_val, phi=phi_val, delta=delta_val)
ypm_val = ypm(x=x_val, y=y_val, qp=qp_val, phi=phi_val, delta=delta_val)


# In[ ]:


xcp_err = 0.01*np.sqrt(0.045**2+0.020**2)
ycp_err = 0.01*np.sqrt(0.116**2+0.059**2)
dx_err = 0.01*np.sqrt(0.018**2+0.001**2)
dy_err = 0.01*np.sqrt(0.035**2+0.013**2)
agamma_err = 0.000113


# def chi2(x, y, qp, phi):
#     ret = ((xcp(x,y,qp,phi)-xcp_val)/xcp_err)**2
#     ret += ((ycp(x,y,qp,phi)-ycp_val)/ycp_err)**2
#     ret += ((dx(x,y,qp,phi)-dx_val)/dx_err)**2
#     ret += ((dy(x,y,qp,phi)-dy_val)/dy_err)**2
# 
#     return ret

# minuit = Minuit(chi2, x=0.00407, y=0.00643, qp=1.0, phi=0.0)

# minuit.errordef = Minuit.LEAST_SQUARES

# minuit.migrad()

# np.rad2deg(0.04)

# def chi2_agamma(x, y, qp, phi):
#     ret = ((xcp(x,y,qp,phi)-xcp_val)/xcp_err)**2
#     ret += ((ycp(x,y,qp,phi)-ycp_val)/ycp_err)**2
#     ret += ((dx(x,y,qp,phi)-dx_val)/dx_err)**2
#     ret += ((dy(x,y,qp,phi)-dy_val)/dy_err)**2
#     ret += ((agamma(x,y,qp,phi)-agamma_val)/agamma_err)**2
#     
#     return ret

# minuit = Minuit(chi2_agamma, x=0.00407, y=0.00643, qp=1.0, phi=0.0)
# minuit.errordef = Minuit.LEAST_SQUARES

# minuit.migrad()

# In[ ]:


#LHCb arXiv:2208.06512 , SL tag 5.4/fb
#3.72 Mio events
#bell has 0.17 for x
#There is also a measurement with prompt 1.6 Mio and SL 1.0 mio https://arxiv.org/pdf/1903.03074 on 3/fb
xcp_err0 = 0.01*np.sqrt(0.045**2+0.020**2)
ycp_err0 = 0.01*np.sqrt(0.116**2+0.059**2)
dx_err0 = 0.01*np.sqrt(0.018**2+0.001**2)
dy_err0 = 0.01*np.sqrt(0.035**2+0.013**2)



#LHCb 2105.09889, prompt + B tag, 6/fb
agamma_err0 = 0.000113

#LHCb 1712.03220v2, prompt tag  5/fb (2011-2016)
ypp_err0 = 1e-3*np.sqrt(0.64**2+0.38**2)
ypm_err0 = 1e-3*np.sqrt(0.64**2+0.38**2)
xpp2_err0 = 1e-3*np.sqrt(0.032**2+0.019**2)
xpm2_err0 = 1e-3*np.sqrt(0.033**2+0.020**2)


# In[ ]:


def getLHCbPoint(newAGamma_err, newDx_err, newYpp_err,  show=False):
    agamma_err = newAGamma_err
    
    scale = newDx_err/dx_err0
    dx_err = scale*dx_err0
    dy_err = scale*dy_err0
    xcp_err = scale*xcp_err0
    ycp_err = scale*ycp_err0

    ypp_err = newYpp_err
    scale2 = newYpp_err/ypp_err0
    ypm_err = scale2*ypm_err0
    xpp2_err = scale2*xpp2_err0
    xpm2_err = scale2*xpm2_err0
    
    
    def chi2(x, y, qp, phi):
        ret = ((xcp(x,y,qp,phi)-xcp_val)/xcp_err)**2
        ret += ((ycp(x,y,qp,phi)-ycp_val)/ycp_err)**2
        ret += ((dx(x,y,qp,phi)-dx_val)/dx_err)**2
        ret += ((dy(x,y,qp,phi)-dy_val)/dy_err)**2
    
        return ret

    def chi2_agamma(x, y, qp, phi):
        ret = chi2(x, y, qp, phi)
        ret += ((agamma(x,y,qp,phi)-agamma_val)/agamma_err)**2
    
        return ret

    def chi2_agamma_Kpi(x, y, qp, phi, delta):
        ret = chi2_agamma(x, y, qp, phi)
        #ret = 0.
        #print("COUCOU: ", ret)
        ret += ((xpp2(x, y, qp, phi, delta)-xpp2_val)/xpp2_err)**2
        ret += ((xpm2(x, y, qp, phi, delta)-xpm2_val)/xpm2_err)**2
        ret += ((ypp(x, y, qp, phi, delta)-ypp_val)/ypp_err)**2
        ret += ((ypm(x, y, qp, phi, delta)-ypm_val)/ypm_err)**2
        #print("blibli: ", ret)
        
        return ret

    minuit = Minuit(chi2, x=0.00407, y=0.00643, qp=1.0, phi=0.0)
    minuit.errordef = Minuit.LEAST_SQUARES
    minuit.migrad()
    if show: print(minuit)

    phi_err1 = np.rad2deg(minuit.errors["phi"])
    qp_err1 = minuit.errors["qp"]

    minuit = Minuit(chi2_agamma, x=0.00407, y=0.00643, qp=1.0, phi=0.0)
    minuit.errordef = Minuit.LEAST_SQUARES
    minuit.migrad()
    if show: print(minuit)

    phi_err2 = np.rad2deg(minuit.errors["phi"])
    qp_err2 = minuit.errors["qp"]

    minuit = Minuit(chi2_agamma_Kpi, x=0.00407, y=0.00643, qp=1.0, phi=0.0, delta=delta_val)
    minuit.errordef = Minuit.LEAST_SQUARES
    minuit.migrad()
    #minuit.fixed["delta"] = True
    if show: print(minuit)

    phi_err3 = np.rad2deg(minuit.errors["phi"])
    qp_err3 = minuit.errors["qp"]

    return phi_err1, qp_err1, phi_err2, qp_err2, phi_err3, qp_err3


# In[ ]:


def makeplot(title,
             lhcb_d=None, lhcb_p=None, lhcb_p_ag=None, lhcb_p_agkpi=None,
             belle2_d=None, belle2_p=None, belle2_p_ag=None, belle2_p_agkpi=None,
             fcc_d=None, fcc_p=None, fcc_p_ag=None, fcc_p_agkpi=None,
             stcf_d=None, stcf_p=None,
             theo=None,
             savename=None, 
            wantlog=True,
             ylim=None,
            legend=True): 
    plt.figure(figsize=(1.25*2.5/0.85,1.25*2))
    ax = plt.gca()

    handles = []
    labels = []
    
    if lhcb_d is not None and lhcb_p is not None:
        l1, = plt.plot(lhcb_d, 1e0*lhcb_p, "o", label="LHC", color="C0",
                         markerfacecolor='None')
        #handles.append(l1)
        #labels.append("LHC: $\\Delta x$")
    
    if lhcb_p_ag is not None and lhcb_d is not None:
        l2, = plt.plot(lhcb_d, 1e0*lhcb_p_ag, "*", label="LHC", color="C0")
        #handles.append(l2)
        #labels.append("LHC: $\\Delta x$+$A\\Gamma$")

    if lhcb_p_agkpi is not None and lhcb_d is not None:
        l2, = plt.plot(lhcb_d, 1e0*lhcb_p_agkpi, ".", label="LHC", color="C0")
        #handles.append(l2)
        #labels.append("LHC: $\\Delta x$+$A\\Gamma$+$K\pi$")

    if fcc_d is not None and fcc_p is not None:
        l3, = plt.plot(fcc_d, 1e0*fcc_p, "o", label="FCC-ee", color="C1",
                         markerfacecolor='None')
        #handles.append(l3)
        #labels.append("Tera-Z: $\\Delta x$")
        l3b, = plt.plot(fcc_d, np.sqrt(6/1.4)*fcc_p, "o", label="LEP3", color="C4",
                         markerfacecolor='None')
        
    if fcc_d is not None and fcc_p_ag is not None:
        l4, = plt.plot(fcc_d, 1e0*fcc_p_ag, "*", label="FCC-ee", color="C1")
        l4b, = plt.plot(fcc_d, np.sqrt(6/1.4)*fcc_p_ag, "*", label="LEP", color="C4")
        #handles.append(l4)
        #labels.append("FCC-ee")#("$6\\times10^{12}\,{\\rm Z}^0$")#: $\\Delta x$+$A\\Gamma$+$K\pi$")
        #handles.append(l4b)
        #labels.append("LEP3")#("$2\\times10^{12}\,{\\rm Z}^0$")

    if fcc_d is not None and fcc_p_agkpi is not None:
        l4, = plt.plot(fcc_d, 1e0*fcc_p_agkpi, ".", label="FCC-ee", color="C1")
        l4b, = plt.plot(fcc_d, np.sqrt(6/1.4)*fcc_p_agkpi, ".", label="LEP", color="C4")
        #handles.append(l4)
        #labels.append("FCC-ee")#("$6\\times10^{12}\,{\\rm Z}^0$")#: $\\Delta x$+$A\\Gamma$+$K\pi$")
        #handles.append(l4b)
        #labels.append("LEP3")#("$2\\times10^{12}\,{\\rm Z}^0$")
        
    if belle2_d is not None and belle2_p is not None:
        l5, = plt.plot(belle2_d, 1e0*belle2_p, "o", label="Belle II", color="C2",
                         markerfacecolor='None')
        #handles.append(l5)
        #labels.append("Belle II: $\\Delta x$")

    if belle2_p_ag is not None and belle2_d is not None:
        l2, = plt.plot(lhcb_d, 1e0*belle2_p_ag, "*", label="Belle II", color="C2")
        #handles.append(l2)
        #labels.append("Belle II")

    if belle2_p_agkpi is not None and belle2_d is not None:
        l2, = plt.plot(belle2_d, 1e0*belle2_p_agkpi, ".", label="Belle II", color="C2")
        #handles.append(l2)
        #labels.append("Belle II")#: $\\Delta x$+$A\\Gamma$+$K\pi$")

    if stcf_d is not None and stcf_p is not None:
        l6, = plt.plot(stcf_d, 1e0*stcf_p, ">", label="Belle II", color="C3")
        #handles.append(l6)
        #labels.append("STCF $5\,{\\rm ab}^{-1}$")
    
    if theo is not None:
        l, = plt.axhline(theo, ls="--", label="SM")
        
     
    #if legend: plt.legend()
    #plt.xlabel("year")
    #plt.title(title)# $[10^{-5}]$")
    plt.ylabel(title)
    
    
    
    plt.xticks(ticks=[0, 1, 2, 3], labels=["today", "2030s", "2040s", "2050s"])
    
    if wantlog: plt.semilogy()
    if ylim is not None: plt.ylim(ylim)
    plt.tight_layout()

    #ax.text(0.98, 0.98, "ESPP26\npreliminary",
    #transform=ax.transAxes,  # axes coordinates
    #ha='right', va='top',
    #fontsize=8,              # smaller font
    #bbox=dict(facecolor='white', edgecolor='none', alpha=0.8, pad=2))
    
    

    #fill up the legend

    if lhcb_d is not None:
        handle = (Line2D([0], [0], marker='o', linestyle='', color='C0',
                         markerfacecolor='None'),
                  Line2D([0], [0], marker='*', linestyle='', color='C0'))
        handles.append(handle)
        labels.append("LHC")

    if belle2_d is not None: 
        handle = (Line2D([0], [0], marker='o', linestyle='', color='C2',
                         markerfacecolor='None'),
                  Line2D([0], [0], marker='*', linestyle='', color='C2'))
        handles.append(handle)
        labels.append("Belle II")

    if fcc_d is not None:
        handle = (Line2D([0], [0], marker='o', linestyle='', color='C1',
                         markerfacecolor='None'),
                  Line2D([0], [0], marker='*', linestyle='', color='C1'))
        handles.append(handle)
        labels.append("FCC-ee")

    if fcc_d is not None:
        handle = (Line2D([0], [0], marker='o', linestyle='', color='C4',
                         markerfacecolor='None'),
                  Line2D([0], [0], marker='*', linestyle='', color='C4'))
        handles.append(handle)
        labels.append("LEP3")

    if stcf_d is not None:
        handle = (Line2D([0], [0], marker='<', linestyle='', color='C3'))
        handles.append(handle)
        labels.append("STCF")# \n $(5\,{\\rm ab}^{-1})$")


    plt.xlim(-0.3, 3.3)

    if legend:
        plt.legend(handles=handles, labels=labels, 
                          handler_map={tuple: HandlerTuple(ndivide=None)},
                          loc='upper right', fontsize=10,
                            labelspacing=0.25 )

    if savename is not None: plt.savefig(savename)

    '''
    if legend: #plt.legend()
        fig_legend = plt.figure()
        # Add the legend to the new figure
        # You can adjust parameters like loc and fontsize
        fig_legend.legend(handles=handles, labels=labels, 
                          handler_map={tuple: HandlerTuple(ndivide=None)},
                          loc='center', fontsize=12,)
        
        # Optional: turn off axes in the legend-only figure
        fig_legend.gca().axis('off')
        
        # Show both figures
        plt.show()
    '''


# ## Load points for LHCb

# In[ ]:


lhcb_d = np.array([0, 1, 2])


# In[ ]:


qp_lhcb = []
qp_ag_lhcb = []
phi_lhcb = []
phi_ag_lhcb = []
phi_ag_kpi_lhcb = []
qp_ag_kpi_lhcb = []


# In[ ]:


ret = getLHCbPoint(11e-5, 18e-5, ypp_err0, show=True)

phi_lhcb.append(ret[0])
qp_lhcb.append(ret[1])
phi_ag_lhcb.append(ret[2])
qp_ag_lhcb.append(ret[3])
phi_ag_kpi_lhcb.append(ret[4])
qp_ag_kpi_lhcb.append(ret[5])


# In[ ]:


#scale AGamma, delta-x using key measurements, use the lumi for B-> Kpi
ret = getLHCbPoint(3.2e-5, 4.1e-5, newYpp_err=np.sqrt(25/0.72)*ypp_err0)

phi_lhcb.append(ret[0])
qp_lhcb.append(ret[1])
phi_ag_lhcb.append(ret[2])
qp_ag_lhcb.append(ret[3])
phi_ag_kpi_lhcb.append(ret[4])
qp_ag_kpi_lhcb.append(ret[5])


# In[ ]:


ret = getLHCbPoint(1.2e-5, 1.6e-5, newYpp_err=np.sqrt(170/0.72)*ypp_err0,
                  show=True)

phi_lhcb.append(ret[0])
qp_lhcb.append(ret[1])
phi_ag_lhcb.append(ret[2])
qp_ag_lhcb.append(ret[3])
phi_ag_kpi_lhcb.append(ret[4])
qp_ag_kpi_lhcb.append(ret[5])


# In[ ]:


np.rad2deg(0.0019)


# In[ ]:


qp_lhcb = np.array(qp_lhcb)
qp_ag_lhcb = np.array(qp_ag_lhcb)
phi_lhcb = np.array(phi_lhcb)
phi_ag_lhcb = np.array(phi_ag_lhcb)
phi_ag_kpi_lhcb = np.array(phi_ag_kpi_lhcb)
qp_ag_kpi_lhcb = np.array(qp_ag_kpi_lhcb)


# In[ ]:


makeplot("$|q/p|$",
         lhcb_d=lhcb_d,
         lhcb_p=qp_lhcb,
         lhcb_p_ag=qp_ag_lhcb,
            lhcb_p_agkpi = qp_ag_kpi_lhcb,
        legend=False)

makeplot("$|\phi|$",
         lhcb_d=lhcb_d,
         lhcb_p=phi_lhcb,
         lhcb_p_ag=phi_ag_lhcb,
            lhcb_p_agkpi = phi_ag_kpi_lhcb,
        legend=False)


# ## Load Belle II data

# In[ ]:



#Belle 0.976/ab 1509.08266 D0-> KK, pipi
agamma_err0 =  0.01*np.sqrt(0.20**2 + 0.07**2) 

#Belle, 1.36/ab . Errors on dy, dx just multpliy np.sqrt(2)/2  arXiv:2410.22961.
#This results in an error on 8 deg for phi, 0.15 for qp, which is quite close to 
#this measurement https://arxiv.org/abs/1404.2412 with 0.9 with full Belle data , 0.2 qp, 13 deg for phi
ycp_err0 = 1e-3*np.sqrt(1.7**2+0.4**2)
xcp_err0 = 1e-3*np.sqrt(1.4**2+0.3**2)
dy_err0 = 0.707*ycp_err0
dx_err0 = 0.707*xcp_err0


#Belle https://arxiv.org/abs/hep-ex/0601029 0.4/ab
ypp_err0 = 1e-2*0.58
ypm_err0 = 1e-2*0.54
xpp2_err0 = 1e-2*0.037
xpm2_err0 = 1e-2*0.034


# Adding KS pi pi pi0 : there is  744509 events in 0.966/ab https://arxiv.org/abs/1703.05721
# There are 0.96*2.05e6 mio events in 1.36/ab of data from the common Belle + Belle II ana. So adding BtoKSpi0 add:

# In[ ]:


n0=0.96*2.05e6
KSpipipi0scale = (744509/0.966 + n0/1.36)/(n0/1.36)
print(KSpipipi0scale)


# In[ ]:


b2_d = np.array([0, 1, 2])

qp_b2 = []
qp_ag_b2 = []
phi_b2 = []
phi_ag_b2 = []
phi_ag_kpi_b2 = []
qp_ag_kpi_b2 = []


# In[ ]:


#Today
ret = getLHCbPoint(agamma_err0, dx_err0, ypp_err0, show=True)

phi_b2.append(ret[0])
qp_b2.append(ret[1])
phi_ag_b2.append(ret[2])
qp_ag_b2.append(ret[3])
phi_ag_kpi_b2.append(ret[4])
qp_ag_kpi_b2.append(ret[5])


# In[ ]:


#10/ab
ret = getLHCbPoint(agamma_err0/np.sqrt(10/0.976), dx_err0/np.sqrt(KSpipipi0scale*10/1.36), ypp_err0/np.sqrt(10/0.4))# show=True)

phi_b2.append(ret[0])
qp_b2.append(ret[1])
phi_ag_b2.append(ret[2])
qp_ag_b2.append(ret[3])
phi_ag_kpi_b2.append(ret[4])
qp_ag_kpi_b2.append(ret[5])


# In[ ]:


print(KSpipipi0scale)
print(dx_err0/np.sqrt(KSpipipi0scale*50/1.36))
print(dx_err0/np.sqrt(50/1.36))
print(40e-5*0.7)


# In[ ]:


#50/ab
ret = getLHCbPoint(agamma_err0/np.sqrt(50/0.976), 
                   dx_err0/np.sqrt(KSpipipi0scale*50/1.36), 
                   ypp_err0/np.sqrt(50/0.4), show=True)

phi_b2.append(ret[0])
qp_b2.append(ret[1])
phi_ag_b2.append(ret[2])
qp_ag_b2.append(ret[3])
phi_ag_kpi_b2.append(ret[4])
qp_ag_kpi_b2.append(ret[5])


# In[ ]:


qp_b2 = np.array(qp_b2)
qp_ag_b2 = np.array(qp_ag_b2)
phi_b2 = np.array(phi_b2)
phi_ag_b2 = np.array(phi_ag_b2)
phi_ag_kpi_b2 = np.array(phi_ag_kpi_b2)
qp_ag_kpi_b2 = np.array(qp_ag_kpi_b2)


# In[ ]:


makeplot("$|q/p|$",
         lhcb_d=lhcb_d,
         lhcb_p=qp_lhcb,
         lhcb_p_ag=qp_ag_lhcb,
            lhcb_p_agkpi = qp_ag_kpi_lhcb,
         belle2_d=b2_d, belle2_p_ag=qp_ag_b2, belle2_p=qp_b2, belle2_p_agkpi=qp_ag_kpi_b2,
        legend=False)

makeplot("$\phi$",
         lhcb_d=lhcb_d,
         lhcb_p=phi_lhcb,
         lhcb_p_ag=phi_ag_lhcb,
            lhcb_p_agkpi = phi_ag_kpi_lhcb,
         belle2_d=b2_d, belle2_p_ag=phi_ag_b2, belle2_p=phi_b2, belle2_p_agkpi=phi_ag_kpi_b2,
        legend=False)


# ## Load FCC-ee numbers

# In[ ]:


#error on dx scaling from LHCb event number
print(0.01*np.sqrt(0.018**2+0.001**2)/np.sqrt((6800/3.72)))

xcp_err0 = 1e-3*np.sqrt(1.4**2+0.3**2)
dx_err0 = 0.707*xcp_err0

print(dx_err0/np.sqrt(6800/2))


# In[ ]:



#scale LHCb arXiv:2208.06512 , SL tag 5.4/fb with 3.72 M events
"""
scale = 1/np.sqrt((6800/3.72))
xcp_err0 = scale*0.01*np.sqrt(0.148**2+0.026**2)
ycp_err0 = scale*0.01*np.sqrt(0.312**2+0.083**2)
dx_err0 = scale*0.01*np.sqrt(0.093**2+0.028**2)
dy_err0 = scale*0.01*np.sqrt(0.192**2+0.026**2)

#scale LHCb https://arxiv.org/abs/1903.03074, SL prompt tag 2.3 mio events
scale = 1/np.sqrt((6800/2.3))
xcp_err0 = scale*0.01*np.sqrt(0.16**2+0.030**2)
ycp_err0 = scale*0.01*np.sqrt(0.36**2+0.11**2)
dx_err0 = scale*0.01*np.sqrt(0.070**2+0.022**2)
dy_err0 = scale*0.01*np.sqrt(0.16**2+0.03**2)
"""

#scale properly: https://arxiv.org/abs/2106.03744 Dstr tag with 30.6 mio decays
scale = 1/np.sqrt((6400/30.6))
xcp_err0 = scale*0.01*np.sqrt(0.046**2+0.029**2)
ycp_err0 = scale*0.01*np.sqrt(0.120**2+0.085**2)
dx_err0 = scale*0.01*np.sqrt(0.018**2+0.001**2)
dy_err0 = scale*0.01*np.sqrt(0.036**2+0.013**2)


#LHCb 2105.09889, prompt + B tag, 6/fb: 76 mio KK+pi pi events
#scale        
agamma_err0 = 0.000113/np.sqrt(800/76)

#LHCb 1712.03220v2, prompt tag  5/fb (2011-2016) 722e5 WS decays

#Yield of B-> K pi DCS, and then scale to LHCb 
scale = 1/np.sqrt(22/0.722)
           
ypp_err0 = scale*1e-3*np.sqrt(0.64**2+0.38**2)
ypm_err0 = scale*1e-3*np.sqrt(0.64**2+0.38**2)
xpp2_err0 = scale*1e-3*np.sqrt(0.032**2+0.019**2)
xpm2_err0 = scale*1e-3*np.sqrt(0.033**2+0.020**2)


# In[ ]:


ret = getLHCbPoint(agamma_err0, dx_err0, ypp_err0, show=True)


# In[ ]:


np.rad2deg(0.0019 )


# In[ ]:


fcc_d = np.array([3])
phi_fcc = np.array([ret[0]])
qp_fcc = np.array([ret[1]])
phi_ag_fcc = np.array([ret[2]])
qp_ag_fcc = np.array([ret[3]])
phi_agkpi_fcc = np.array([ret[4]])
qp_agkpi_fcc = np.array([ret[5]])


# In[ ]:


makeplot("$|q/p|$",
         lhcb_d=lhcb_d,
         lhcb_p=qp_lhcb,
         lhcb_p_ag=qp_ag_lhcb,
            lhcb_p_agkpi = qp_ag_kpi_lhcb,
         belle2_d=b2_d, belle2_p_ag=qp_ag_b2, belle2_p=qp_b2, belle2_p_agkpi=qp_ag_kpi_b2,
         fcc_d=fcc_d, fcc_p_ag=qp_ag_fcc, fcc_p_agkpi=qp_agkpi_fcc, fcc_p=qp_fcc,
        legend=False)

makeplot("$\phi$",
         lhcb_d=lhcb_d,
         lhcb_p=phi_lhcb,
         lhcb_p_ag=phi_ag_lhcb,
            lhcb_p_agkpi = phi_ag_kpi_lhcb,
         belle2_d=b2_d, belle2_p_ag=phi_ag_b2, belle2_p=phi_b2, belle2_p_agkpi=phi_ag_kpi_b2,
         fcc_d=fcc_d, fcc_p_ag=phi_ag_fcc, fcc_p_agkpi=phi_agkpi_fcc, fcc_p=phi_fcc,
        legend=True)


# ## Load STCF numbers

# stcf_d = np.array([2,3])
# qp_1ab = 0.2*0.7/3.1
# phi_1ab = 20*0.5/2.9
# qp_stcf = np.array([qp_1ab/np.sqrt(10), qp_1ab/np.sqrt(20)]) 
# phi_stcf = np.array([phi_1ab/np.sqrt(10), phi_1ab/np.sqrt(20)])

# In[ ]:


stcf_d = np.array([3])
qp_1ab = 0.026
phi_1ab = 2.14
qp_stcf = np.array([qp_1ab/np.sqrt(5)])#, qp_1ab/np.sqrt(20)]) 
phi_stcf = np.array([phi_1ab/np.sqrt(5)])#, phi_1ab/np.sqrt(20)])


# In[ ]:


phi_1ab


# ## make plot

# In[ ]:


makeplot("$\sigma(|q/p|)$",
         lhcb_d=lhcb_d,
         lhcb_p=qp_lhcb,
         lhcb_p_ag=qp_ag_lhcb,
            #lhcb_p_agkpi = qp_ag_kpi_lhcb,
         belle2_d=b2_d, belle2_p_ag=qp_ag_b2, belle2_p=qp_b2, #belle2_p_agkpi=qp_ag_kpi_b2,
         fcc_d=fcc_d, fcc_p_ag=qp_ag_fcc, #fcc_p_agkpi=qp_agkpi_fcc, 
         fcc_p=qp_fcc,
         stcf_d=stcf_d, stcf_p=qp_stcf,
        legend=True,
         ylim=(1e-3, 6e-1),
        savename="figures/charm_qp.pdf")

makeplot("$\sigma(\phi)~[^{\circ}]$",
         lhcb_d=lhcb_d,
         lhcb_p=phi_lhcb,
         lhcb_p_ag=phi_ag_lhcb,
            #lhcb_p_agkpi = phi_ag_kpi_lhcb,
         belle2_d=b2_d, belle2_p_ag=phi_ag_b2, belle2_p=phi_b2, #belle2_p_agkpi=phi_ag_kpi_b2,
         fcc_d=fcc_d, fcc_p_ag=phi_ag_fcc, #fcc_p_agkpi=phi_agkpi_fcc, 
         fcc_p=phi_fcc,
          stcf_d=stcf_d, stcf_p=phi_stcf,
         ylim=(0.8e-1, 80),
         savename="figures/charm_phi.pdf",
        legend=True)

