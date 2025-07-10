# My attemps to re-implement table 7
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
fontNames = {'size'   : 15}   # Names of hadrons next to markers

# BFs from LCVision
BFs = { "Vud" : 0.318,
        "Vus" : 0.017,
        "Vub" : 4.5e-6,
        "Vcd" : 0.017,
        "Vcs" : 0.317,
        "Vcb" : 5.9e-4}
NW = 10**8

# effs from ECFA report
# columns : true [ b,s,c,u,d,g]
# rows : result b,c,s
effs = { "b" : { "b" : 0.8, "s" : 0.0001, "c" : 0.003, "u" : 0.0005, "d" : 0.0005, "g" : 0.007 },
         "c" : { "b" : 0.02, "s" : 0.008,"c" :  0.8, "u" : 0.01, "d" : 0.01, "g" : 0.01 },
         "s" : { "b" : 0.01, "s" : 0.9, "c" : 0.1," u" :  0.3,"d" :  0.3, "g" : 0.2 }  }

# numbers from Ruan
cols = { "b" : 0, "b~" :1,"c" :2, "c~" :3, "s" :4, "s~" : 5, "u" : 6, "u~" : 7, "d" : 8, "d~" : 9, "G" : 10}
Ruan = [ [0.745, 0.163, 0.033, 0.025, 0.004, 0.003, 0.002, 0.003, 0.002, 0.002, 0.017],
         [0.170, 0.737, 0.026, 0.033, 0.003, 0.004, 0.003, 0.002, 0.002, 0.003, 0.018],
         [0.015, 0.014, 0.743, 0.055, 0.036, 0.031, 0.025, 0.009, 0.009, 0.018, 0.043],
         [0.016, 0.015, 0.056, 0.739, 0.032, 0.037, 0.009, 0.026, 0.017, 0.010, 0.043],
         [0.003, 0.002, 0.020, 0.018, 0.543, 0.102, 0.030, 0.080, 0.063, 0.045, 0.092],
         [0.003, 0.003, 0.018, 0.020, 0.102, 0.542, 0.084, 0.028, 0.045, 0.062, 0.094],
         [0.002, 0.003, 0.020, 0.011, 0.044, 0.131, 0.367, 0.055, 0.080, 0.174, 0.111],
         [0.003, 0.003, 0.011, 0.019, 0.132, 0.043, 0.062, 0.356, 0.178, 0.081, 0.111],
         [0.003, 0.003, 0.012, 0.019, 0.112, 0.092, 0.082, 0.207, 0.277, 0.079, 0.112],
         [0.003, 0.003, 0.020, 0.012, 0.092, 0.112, 0.219, 0.076, 0.079, 0.272, 0.113],
         [0.015, 0.014, 0.024, 0.024, 0.052, 0.052, 0.043, 0.041, 0.034, 0.034, 0.667] ]

with open("ckmYields.tex", "w") as f:
    f.write("\\begin{tabular}{L|CC}\n")
    f.write("\\rowcolor{midcommon} V_{ij} & \\text{BF} & \\text{yield} \\\\ \\hline\n")
    for c,b in BFs.items():
        emph = ""
        if "cb" in c or "cs" in c: emph = "\\rowcolor{lightcommon} "
        bb = ("{0:.2E}".format(b)).replace("E-0","\\times10^{-")+"}"
        q1 = cols[c[1]]
        q2 = cols[c[2]] # ignoring twidles
        N = NW*b*Ruan[q1][q1]*Ruan[q2][q2]
        NN = ("{0:.1E}".format(N)).replace("E+0","\\times10^{")+"}"
        f.write("{3} \\{0} & {1} & {2} \\\\\n".format(c,bb,NN,emph))
    f.write("\\end{tabular}\n")
f.close()
