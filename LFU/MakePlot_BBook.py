import matplotlib.pyplot as plt
import numpy as np

def make_plot(plot_config=None):
    # Import data
    data_config = plot_config["data_config"]
    time_periods = plot_config["time_periods"]
    x = np.arange(len(time_periods))

    # Create plot
    fig, ax = plt.subplots(figsize=(7, 6))

    # Draw data
    for val in range(len(time_periods)):
        ipoint = 0
        npoints = len([x for x in data_config.keys() if data_config[x][1][val] is not None])
        
        for key, values in data_config.items():
            shift = (ipoint - (npoints - 1) / 2) * plot_config["point_displace"]
            if values[1][val] is None:
                continue
            elif values[0] == "bar":
                plt.bar(x[val]+shift, values[1][val], color=values[2], label=values[3], width=plot_config["point_displace"])
            elif isinstance(values[1][val],list):
                plt.errorbar(x[val]+shift, values[1][val][0], yerr=[[values[1][val][1]],[values[1][val][2]]],fmt=values[0], color=values[2], elinewidth=3, label=values[3], markersize=plot_config["marker_size"])
            else:
                plt.plot(x[val]+shift, values[1][val], marker=values[0], color=values[2], label=values[3], linestyle='None', markersize=plot_config["marker_size"])
            ipoint += 1



    # Set labels, axis, grid
    ax.set_xticks(x)
    ax.set_xticklabels(time_periods, fontsize=plot_config["xlabel_font"], rotation=plot_config["xlabel_rotation"])
    if plot_config["y_title"]:
        ax.set_ylabel(plot_config["y_title"], fontsize=plot_config["ytitle_font"])
    if plot_config["x_title"]:
        ax.set_xlabel(plot_config["x_title"], fontsize=plot_config["xtitle_font"])
    ax.set_title(plot_config["plot_title"], fontsize=plot_config["title_font"])
    plt.yticks(fontsize=plot_config["ylabel_font"])

    if plot_config["ylog_scale"]:
        plt.yscale("log")
    plt.ylim(plot_config["y_min"], plot_config["y_max"])
    ax.grid(True, axis='y', linestyle='--', alpha=0.6)

    # Legend
    handles, labels = plt.gca().get_legend_handles_labels()
    by_label = dict(zip(labels, handles))
    ax.legend(by_label.values(), by_label.keys(), title=plot_config["legend_title"], loc=plot_config["legend_loc"], fontsize=plot_config["legend_font"])

    # Draw plot
    plt.tight_layout()
    plt.savefig(f"{plot_config['plot_name']}.{plot_config['extension']}", dpi=300, bbox_inches='tight')


if __name__ == "__main__":
    base_config = {
        "legend_title": "", #Title for the legend
        "x_title": "Time Period", #Title for the x-axis
        "point_displace": 0.15, #Displacement of points for better visibility and bar width
        "extension": "png", #File extension for saving the plot
        "marker_size": 12, #Size of the markers
        "legend_loc": "upper right", #Location of the legend
	"legend_font" : 15, #font size for the legend
        "y_min": 0, # Minimum value for the y-axis
        "y_max": None,  # Maximum value for the y-axis, None means automatic scaling
        "time_periods": ["2030s", "2040s", "2050s"], # Time periods for the x-axis
        "ylog_scale": False, # Whether to use logarithmic scale for the y-axis
        "title_font": 18, # Font size for the plot title
        "xtitle_font": 16, # Font size for the x-axis title
        "ytitle_font": 16, # Font size for the y-axis title
        "xlabel_font": 14, # Font size for the x-axis labels
        "ylabel_font": 14, # Font size for the y-axis labels
        "xlabel_rotation": 0, # Rotation angle for the x-axis labels
    }

    measuremets_config = {
        "BR_Bsmumu": { # Measurement name
            "plot_title": r"$\mathcal{B}(B^0_s \rightarrow \mu^+ \mu^-)$", # Title of the plot
            "y_title": r"Uncertainty on $\mathcal{B}(B^0_s \rightarrow \mu^+ \mu^-)$ [10$^{-9}$]", # Title for the y-axis
            "plot_name": "Bs_mumu_limits",  # Name of the plot file to be saved
            "time_periods": ["Current", "2030s", "2040s","2050s"], # Time periods for the x-axis
	    "y_min": 0.1,
            "data_config": { #
	        "atlas_error": ["",[None,None,[0.365,0.035,0.035],None],"red",""],
		"atlas_uncertainty": ["d", [0.75, None, None, None], "red", "ATLAS"],
                "cms_uncertainty": ["o", [0.45, None, 0.22, None], "orange", "CMS"],
                "lhcb_uncertainty": ["^", [0.48, 0.23, 0.16, None], "green", "LHCb"],
	        "fccee_uncertainty": ["v", [None, None, None, 0.18], "magenta", "FCC-ee"],
            },
        },
	"BR_B0mumu": { # Measurement name
            "plot_title": r"$\mathcal{B}(B^0 \rightarrow \mu^+ \mu^-)$", # Title of the plot
            "y_title": r"Limits/uncertainty on $\mathcal{B}(B^0 \rightarrow \mu^+ \mu^-)$ [10$^{-10}$]", # Title for the y-axis
            "plot_name": "B0_mumu_limits",  # Name of the plot file to be saved
            "time_periods": ["Current", "2030s", "2040s","2050s"], # Time periods for the x-axis
            "data_config": { #
		"atlas_error": ["",[None,None,[0.40,0.08,0.08],None],"red","ATLAS (Uncertainty)"],
                "atlas_bar": ["bar", [2.1, None, None,None], "red", "ATLAS (95% C.L.)"],  # [data type, values, color, label]
                "cms_bar": ["bar", [1.5, None, None, None], "orange", "CMS (90% C.L.)"],                
                "cms_uncertainty": ["o", [None, None, 0.12, None], "orange", "CMS (Uncertainty)"],
                "lhcb_uncertainty": ["^", [0.79, 0.3, 0.12, None], "green", "LHCb (Uncertainty)"],
		"fccee_uncertainty": ["v", [None, None, None, 0.15], "magenta", "FCC-ee (Uncertainty)"],
            },
        },
        "BR_B0Ksttautau": {
            "plot_title": r"$\mathcal{B}(B^0 \rightarrow K^{*0} \tau^+ \tau^-)$",
            "y_title": r"Limits/uncertainty on $\mathcal{B}(B^0 \rightarrow K^{*0} \tau^+ \tau^-)$ [10$^{-7}$]",
            "plot_name": "B0_Ksttautau_limits",
	    #"y_min": -7.,  #linear plot
	    "y_max": 10000,  #log plot
	    "legend_loc": "upper right",
	    #"time_periods": ["Current", "2030s", "2040s", "2050s"], # Time periods for the x-axis
            "data_config": {
		"belle2_barKst": ["bar", [3400, 1500, None], "blue", "Belle II"], #"Belle II (90% C.L.)"],
		"belle2_barK": ["bar", [1900, 900, None], "cyan", r"Belle II $K^+\tau^+\tau^-$"],
		"ilc_bar": ["bar", [None, None, 55], "orange", "LFC"],                
		"lep3_bar": ["bar", [None, None, 2.0], "pink", "LEP3"],
                "fccee_uncertainty": ["v", [None, None, 1], "magenta", "FCC-ee"],
            },
            "ylog_scale": True,
        },
        "BR_B0Kstnunu": {
            "plot_title": r"$\mathcal{B}(B^0 \rightarrow K^{*0} \nu \bar{\nu})$",
            "y_title": r"Relative uncertainty on $\mathcal{B}(B^0 \rightarrow K^{*0} \nu \bar{\nu}) (\%)$",
            "plot_name": "B0_Kstnunu_limits",
	    "legend_loc": "lower left",
	    #"time_periods": ["Current", "2030s", "2040s", "2050s"], # Time periods for the x-axis
	    "y_max": 50.,
            "data_config": {
                "belle2_uncertaintyKst": ["s", [33, 23, None], "blue", "Belle II "],
   		"belle2_uncertaintyK": ["s", [14, 8, None], "cyan", r"Belle II $K^+\nu\bar{\nu}$"],
                "ilc_uncertainty": ["o", [None, None, 28], "orange", "LFC"],
                "lep3_uncertainty": ["^", [None, None, 1.32], "pink", "LEP3"],
                "fccee_uncertainty": ["v", [None, None, 0.75], "magenta", "FCC-ee"],
            },
            "ylog_scale": True,
        },
	"RDD": {
            "plot_title": r"LFU ratio $R(D^{(*)})$",
            "y_title": r"Rel. uncertainty on $R(D^{(*)}) (\%)$",
            "plot_name": "RDD_uncertainty",
            "legend_loc": "upper right",
            "time_periods": ["Current", "2030s", "2040s", "2050s"], # Time periods for the x-axis
            "data_config": {
                "belle2D": ["s", [12, 3.0, 1.4, None], "cyan", r"Belle II $R(D)$"],
                "lhcbD": ["^", [14, 4.4, 3.3, None], "orange", "LHCb $R(D)$"],
		"lep3D": ["D",[None,None,None,0.40],"purple",r"LEP3 $R(D_s)$"],
		"fcceeD": ["v",[None,None,None,0.24],"brown",r"FCC-ee $R(D_s)$"],
                "belle2": ["s", [7, 1.8, 1.0, None], "blue", r"Belle II $R(D^*)$"],
                "lhcb": ["^", [6, 3.2, 3.0, None], "green", "LHCb $R(D^*)$"],
		"lep3": ["D",[None,None,None,0.32],"pink",r"LEP3 $R(D_s^*)$"],
		"fccee": ["v",[None,None,None,0.19],"magenta",r"FCC-ee $R(D_s^*)$"],
            },
        },	
        "RK": {
            "plot_title": r"LFU ratio $R(K^{(*)})$",
            "y_title": r"Uncertainty on $R(K^{(*)})$",
            "plot_name": "RK_uncertainty",
	    "legend_loc": "upper right",
	    "y_max": 1.0,
	    "time_periods": ["Current", "2030s", "2040s", "2050s"], # Time periods for the x-axis
            "data_config": {
                "belle2": ["s", [0.38, 0.07, 0.032, None], "blue", r"Belle II $R(K^{*})$"],
                "lhcb": ["^", [0.047, 0.020, 0.007, None], "green", r"LHCb $R(K^+)$"],
                #"ilc": ["o", [None, None, None, 0.164], "orange", r"$2\times 10^{9}Z^0$ $R(K^{*})$"], 
		"lep3": ["^", [None, None, None, 0.0062], "pink", "LEP3"],
                "fccee": ["v", [None, None, None, 0.003], "magenta", "FCC-ee"],
            },
	    "ylog_scale": True,
	},	
    }

    for measure, config in measuremets_config.items():
        plot_config = base_config.copy()
        plot_config.update(config)
        make_plot(plot_config=plot_config)