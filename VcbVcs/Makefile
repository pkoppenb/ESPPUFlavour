all : VcbPlot.pdf

Vcb.pdf : MyFig2.py $(wildcard *.txt) esppu.mplstyle
	python MyFig2.py 

VcbPlot.pdf : VcbPlot.tex Vcb.pdf ESPP-logo-2025-color_color-crop.pdf
	pdflatex VcbPlot ; pdflatex VcbPlot
