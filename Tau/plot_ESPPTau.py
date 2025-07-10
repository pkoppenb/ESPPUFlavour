import matplotlib.pyplot as plt
import uproot
import pandas as pd
import numpy as np
#import plothist as ph
plt.style.use('../VcbVcs/esppu.mplstyle')

#################################
### Only observed limits, All ###
#################################

#################
### tau -> mu gamma ###
#################

x1 = [1, 2, 3 ]
lab1 =  [r'Current', r'2030s',r'2040s' ]
#lab1 = [r'$B^+ \rightarrow K^+ \tau^+ \mu^-$', r'$B^+ \rightarrow K^+ \tau^- \mu^+$', r'$B^+ \rightarrow K^+ \tau^+ e^-$', r'$B^+ \rightarrow K^+ \tau^- e^+$']

### Belle ###
val1_obs1 = [ 75e-9, 15e-9, 7e-9  ]
col1_obs1 = ['blue', 'blue', 'blue']

x2 = [4 ]
lab2 =  [r'2050s' ]
### FCC-ee ###
val2_obs1 = [ 1.2e-9]
col2_obs1 = ['green']

### LEPZ ###
#val3_obs1 = [2.1e-9]
val3_obs1 = [2.5e-9]
col3_obs1 = ['orange']


### STFC ###
x3 = [2,3]
val4_obs1 = [12e-9, 3.8e-9]
col4_obs1 = ['red', 'red']

### LCF ###
#val5_obs1 = [42e-9]
val5_obs1 = [66e-9]
col5_obs1 = ['deepskyblue']




##################
### tau to 3 mu ###
##################
#x2 = [5, 6]
#lab2 = [r'$B^0 \rightarrow K^{*0} \tau^+ \mu^-$',r'$B^0 \rightarrow K^{*0} \tau^- \mu^+$',]

### LHCb ###
val1_obs2 = [46e-9, 6.4e-9, 2.6e-9 ]
col1_obs2 = ['deeppink', 'deeppink',  'deeppink']

### Belle ###
val2_obs2 = [ 19e-9, 0.8e-9, 0.2e-9  ]
col2_obs2 = ['blue', 'blue', 'blue']

### FCC-ee ###
val3_obs2 = [ 0.02e-9]
col3_obs2 = ['green']

### LEP ###
#val4_obs2 = [0.06e-9]
val4_obs2 = [0.09e-9]
col4_obs2 = ['orange']

### STFC ###
val5_obs2 = [1e-9, 0.1e-9]
col5_obs2 = ['red', 'red']

x4 = [1,3]
### ATLAS ###
val6_obs2 = [376e-9,  1.3e-9 ] # 1.3-6.4
col6_obs2 = ['hotpink',   'hotpink']

### CMS ###
val7_obs2 = [29e-9, 3.9e-9 ]
col7_obs2 = ['orchid',  'orchid']


### LCF ###
#val8_obs2 = [24e-9]
val8_obs2 = [60e-9]
col8_obs2 = ['deepskyblue']



###########################################
x_coords = x1 + x2 
x_labs = lab1 + lab2

## tau -> mu gamma
plt.figure(figsize=(9, 6))
plt.scatter(x1, val1_obs1, c=col1_obs1, marker='D', s=100)
plt.scatter(x2, val2_obs1, c=col2_obs1, marker='^', s=100)
plt.scatter(x2, val3_obs1, c=col3_obs1, marker='v', s=100)
plt.scatter(x3, val4_obs1, c=col4_obs1, marker='*', s=100)
plt.scatter(x2, val5_obs1, c=col5_obs1, marker='P', s=100)
plt.xticks(x_coords, x_labs)  # Set x-axis labels using LaTeX formatted labels
plt.xticks(rotation=70)  # Rotate the x-axis labels for readability
legend_items = [plt.scatter([], [], color='blue', marker='D', label='Belle II'),
                plt.scatter([], [], color='deepskyblue', marker='P', label='LCF'),
                plt.scatter([], [], color='red', marker='*', label='STCF'),
                plt.scatter([], [], color='orange', marker='v', label='LEP3'),
                plt.scatter([], [], color='green', marker='^', label='FCC-ee')]
plt.legend(handles=legend_items, frameon=False, loc='upper right', ncol=4, fontsize=16)
plt.grid(True, alpha=0.5, linestyle='-', axis='y', zorder=-1)
plt.ylim(0.5e-9, 450e-9)
plt.ylabel(r"UL (90\% CL)",fontsize=18 )
plt.yscale('log')
#plt.figtext(0.25, 0.25, r'ESPP 2026, preliminary', fontsize=15)
plt.xticks(fontsize=18)
plt.yticks(fontsize=18)
#plt.tight_layout()
plt.title(r'$\tau \rightarrow  \mu\gamma$', fontsize=24)
plt.savefig(f'Tau2mug_ESPP.pdf', bbox_inches='tight')

### tau -> 3mu

plt.figure(figsize=(9, 6))
plt.scatter(x1, val1_obs2, c=col1_obs2, marker='o', s=100)
plt.scatter(x1, val2_obs2, c=col2_obs2, marker='D', s=100)
plt.scatter(x2, val3_obs2, c=col3_obs2, marker='^', s=100)
plt.scatter(x2, val4_obs2, c=col4_obs2, marker='v', s=100)
plt.scatter(x3, val5_obs2, c=col5_obs2, marker='*', s=100)
plt.scatter(x4, val6_obs2, c=col6_obs2, marker='<', s=100)
plt.scatter(x4, val7_obs2, c=col7_obs2, marker='>', s=100)
plt.scatter(x2, val8_obs2, c=col8_obs2, marker='P', s=100)
#plt.axvline(x=4.5, ymin=0, ymax=0.85, color='gray', linestyle='--', linewidth=1)
#plt.axvline(x=6.5, ymin=0, ymax=0.85, color='gray', linestyle='--', linewidth=1)
plt.xticks(x_coords, x_labs)  # Set x-axis labels using LaTeX formatted labels
plt.xticks(rotation=70)  # Rotate the x-axis labels for readability
legend_items = [plt.scatter([], [], color='blue', marker='D', label='Belle II'),
                plt.scatter([], [], color='deeppink', marker='o', label='LHCb'),
                plt.scatter([], [], color='red', marker='*', label='STCF'),
                plt.scatter([], [], color='orchid', marker='>', label='CMS'),
                plt.scatter([], [], color='orange', marker='v', label='LEP3'),
                plt.scatter([], [], color='hotpink', marker='<', label='ATLAS'),
                plt.scatter([], [], color='deepskyblue', marker='P', label='LCF'),
                plt.scatter([], [], color='green', marker='^', label='FCC-ee')]                
plt.legend(handles=legend_items, frameon=False, loc='upper right', ncol=4, fontsize=16)
plt.grid(True, alpha=0.5, linestyle='-', axis='y', zorder=-1)
plt.ylim(0.01e-9, 2500e-9)
plt.ylabel(r"UL (90\% CL)", fontsize=18)
plt.yscale('log')
#plt.figtext(0.25, 0.25, r'ESPP 2026, preliminary', fontsize=15)
plt.xticks(fontsize=18)
plt.yticks(fontsize=18)
plt.title(r'$\tau \rightarrow 3 \mu$', fontsize=24)
#plt.tight_layout()
plt.savefig(f'Tau3mu_ESPP.pdf', bbox_inches='tight')

#### tau produced
#xtau = [1,2,3,4,5,6,7]
#xlabel = [ r'BelleII' , r'STCF' , r'BelleII' , r'STCF', r'LCF', r'2 TeraZ', r'6 TeraZ']
#val = [9, 3.6, 46, 36, 0.17, 67, 200 ]

xtau = [1,2,3,4,5,6]
xlabel = [ r'Belle II' , r'STCF' , r'Belle II' , r'STCF',  r'2 TeraZ', r'6 TeraZ']
val = [9, 3.6, 46, 36,  67, 200 ]
plt.figure(figsize=(9, 6))
plt.xticks(xtau, xlabel)  # Set x-axis labels using LaTeX formatted labels

plt.bar(xtau, val, color = 'hotpink')
plt.xticks(rotation=70)  # Rotate the x-axis labels for readability
plt.ylim(0.0, 300)
plt.axvline(x=2.5, ymin=0, ymax=0.85, color='gray', linestyle='--', linewidth=1)
plt.axvline(x=4.5, ymin=0, ymax=0.85, color='gray', linestyle='--', linewidth=1)
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.title('tau pairs produced (billions)', fontsize=20)
plt.tight_layout()
plt.savefig(f'Taupairs.pdf', bbox_inches='tight')
