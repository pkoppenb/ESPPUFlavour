
# coding: utf-8

# In[1]:


import matplotlib
import matplotlib.pyplot as plt
import numpy as np


# In[2]:


lhcb_y = np.array([2020, 2033,2040])
lhcb_p = np.array([15e-5, 4.1e-5, 1.6e-5])

FCC_y = np.array([2045])
FCC_p = np.array([1.6e-5])

b2_y = np.array([2025, 2032])
b2_p = np.array([140e-5, 60e-5])


# In[3]:


plt.figure(figsize=(5,3))

plt.plot(lhcb_y, 1e5*lhcb_p, "o", label="LHCb")
plt.plot(FCC_y, 1e5*FCC_p, "o", label="FCC-ee")
plt.plot(b2_y, 1e5*b2_p, "o", label="Belle II")

plt.legend()
plt.xlabel("year")
plt.ylabel("$\Delta x(D^0\\to K_S^0\,\pi\,\pi)$ $[10^{-5}]$")

plt.semilogy()

plt.savefig("/Users/robert/Downloads/Delta-x-projections.pdf")


# In[4]:


lhcb_y = np.array([2020, 2033,2040])
lhcb_p = np.array([17e-4, 5e-4, 1.6e-5])

FCC_y = np.array([2045])
FCC_p = np.array([1.6e-5])

b2_y = np.array([2025, 2032])
b2_p = np.array([40e-4, 9.5e-5])

plt.figure(figsize=(5,3))

plt.plot(lhcb_y, 1e5*lhcb_p, "o", label="LHCb")
plt.plot(FCC_y, 1e5*FCC_p, "o", label="FCC-ee")
plt.plot(b2_y, 1e5*b2_p, "o", label="Belle II")

plt.legend()
plt.xlabel("year")
plt.ylabel("$\Delta x(D^0\\to K_S^0\,\pi\,\pi)$ $[10^{-5}]$")

plt.semilogy()

