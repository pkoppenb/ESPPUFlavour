import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.axes_grid1.inset_locator import inset_axes, mark_inset

plt.style.use('../VcbVcs/esppu.mplstyle')
# Example configurations
configurations = [r'LHCb \\(300 fb$^{-1}$)',r'Belle II \\(50 ab$^{-1}$)',r'LCF \\(2 10$^9$ Z$^0$)',r'LEP3 \\(1.4 10$^{12}$ Z$^0$)', r'FCC-ee \\(6 10$^{12}$ Z$^0$)']

# Marta : 1.5 x10^11 b-bbar /fb-1 
# 50 fb-1 : 75 x10^11 b-bbar 
# 300 fb-1 : 450 x10^11 b-bbar 

# Z0 -> b bar = 15% 
# FCCee 6 TeraZ : 9 10^11 b-bbar
# LEP3 1.4 TeraZ  : 2.1 10^11 b-bbar
# LCF (2 10^9) : 3 10^8 b-bbar

# B Factories : fb-1 1.1 *10^6 /fb-1 
# Belle II (10 ab-1) ; 1.1 10^6 * 10 * 10^3 = 1.1 10^10 
# Belle II (50 ab-1) ; 1.1 10^6 * 50 * 10^3 = 5.5 10^10 = 55 10^9 


# b-hadrons species in 10^7 units 
signal_strengthsBd = [4500000*2*.375, 5500, 30*2*.40, 21000*2*.40, 90000*2*.40]
signal_strengthsBu = [4500000*2*.375, 5500, 30*2*.40, 21000*2*.40, 90000*2*.40]
signal_strengthsBs = [4500000*2*.10, 0., 30*2*.1, 21000*2*.10, 90000*2*.10]
signal_strengthsLb = [4500000*2*.15, 0., 30*2*.1, 21000*2*.10, 90000*2*.10]

# Plotting
fig, ax = plt.subplots(figsize=(8, 5))

# Create the plot
# X locations for the groups
x = np.arange(len(configurations))
width = 0.35  # Width of each bar

bars1 = ax.bar(x - width/2, signal_strengthsBd, width/4, label=r'$B_d / \overline{B}_d$', color='skyblue')
bars2 = ax.bar(x - width/4, signal_strengthsBu, width/4, label=r'$B^+ / B^-$', color='darkblue')
bars3 = ax.bar(x , signal_strengthsBs, width/4, label=r'$B_s / \overline{B}_s$', color='orange')
bars4 = ax.bar(x + width/4, signal_strengthsLb, width/4, label=r'$\Lambda_b / \overline{\Lambda}_b$', color='red')

ax.set_ylabel(r'Number of $b$-hadrons in $10^{7}$ units')
#ax.set_xlabel('Facilities')
ax.set_title('$b$-hadrons in detector acceptance')
ax.set_xticks(x)
ax.set_xticklabels(configurations)
ax.legend()
ax.grid(axis='y', linestyle='--', alpha=0.7)

#fig.text(0.4, 0.85, 'ESPP2026, preliminary', fontsize=12, color='black') 

plt.yscale('log')

# Show the plot
#plt.ylim(0, 95000)
plt.tight_layout()
#plt.show()
fig.savefig('NBB_details_log.pdf', bbox_inches='tight')
