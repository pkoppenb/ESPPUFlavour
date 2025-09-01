import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.axes_grid1.inset_locator import inset_axes, mark_inset
from matplotlib.patches import Rectangle
from matplotlib.patches import Patch
from matplotlib.lines import Line2D

plt.style.use('../VcbVcs/esppu.mplstyle')


# Example configurations
configurations = [r'$0^+ \rightarrow 0^+$',r'$n \rightarrow p e^- \overline{\nu} (\gamma)$',r'$\pi^+ \rightarrow \pi^0 e^+ \nu (\gamma)$']


Now= [0.97367,0.9742167832167833,0.973951048951049]
Now_err = [0.00032,.5*(0.9751118881118881-0.9733216783216784),0.0027]   


Future = [0., 0.9742167832167833,  0.973951048951049] 
Future_err = [0., 0.5*(0.9745664335664336-0.973881118881119),(0.9736643579941533-0.9727180121430177)*.5]


# Plotting
fig, ax = plt.subplots(figsize=(8, 5))

# Create the plot
# X locations for the groups
x = np.arange(len(configurations))


plt.xticks(fontsize=12) 
plt.yticks(fontsize=12) 
ax.set_ylabel(r'$|V_{ud}|$')
ax.set_xlabel('')
ax.set_xticks(x)
ax.set_xticklabels(configurations)

ax.grid(axis='y', linestyle='--', alpha=0.7)
rangeMinPlot = .97
rangeMaxPlot = .977
plt.ylim(rangeMinPlot,rangeMaxPlot)

xrangeMinPlot = -.5
xrangeMaxPlot = 3.
plt.xlim(xrangeMinPlot,xrangeMaxPlot)

width = 0.35  # Width of each bar
bars1 = ax.errorbar(x , Now, xerr=0., yerr=Now_err,label=r'Current', marker = '^', markersize = 10, markerfacecolor = 'blue',ecolor = 'blue',linestyle = 'none')
bars2 = ax.errorbar(x + width/4, Future, xerr=0., yerr=Future_err,label=r'Future', marker = 'o', markersize = 10, markerfacecolor = 'red',ecolor = 'red',linestyle = 'none')

xVub1 = .97475
VudErr1 = .00012
xCKM1 = xrangeMinPlot
yCKM1 = xVub1 - VudErr1

H_CKM1 = 2.*VudErr1
W_CKM1 = 5.
ax.add_patch(Rectangle((xCKM1, yCKM1), W_CKM1, H_CKM1,facecolor='lightgrey'))
#ax.text(-.3,yCKM1 , r'$V_{us} (K \rightarrow \pi \ell \nu$)', fontsize=11, color='black') 

xVub2 = .97431
VudErr2 = .00011
xCKM2 = xrangeMinPlot
yCKM2 = xVub2 - VudErr2

H_CKM2 = 2.*VudErr2
W_CKM2 = 5.
ax.add_patch(Rectangle((xCKM2, yCKM2), W_CKM2, H_CKM2,facecolor='skyblue'))
#ax.text(-.3,yCKM2 , r'$V_{us}$ ($|V_{ud}/V_{us}|$)',fontsize=11, color='black') 


#plt.axhline(y=.021, color='brown', linestyle='--', label='Current Th uncertainty')
legend_elements = [
    Patch(facecolor='skyblue', label=r'$V_{us}$ from $K \rightarrow \pi \ell \nu$ (PDG)'),
    Patch(facecolor='lightgrey', label=r'$V_{us}$ from $|V_{ud}/V_{us}|$ (PDG)'),
    Line2D([0], [0], marker='^', color='none', label='Current', markerfacecolor='blue', markersize=10),
    Line2D([0], [0], marker='o', color='none', label='Future', linestyle='None',markerfacecolor='red', markersize=10)
]
ax.legend(handles=legend_elements,loc='lower left',fontsize=14)





# Show the plot
#plt.tight_layout()
# plt.show()
fig.savefig('Vud_details.pdf', bbox_inches='tight')
