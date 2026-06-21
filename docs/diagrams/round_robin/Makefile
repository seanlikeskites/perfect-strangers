all: initial.svg fixed.svg rotated.svg

%.svg: %.tex
	pdflatex $<
	pdftocairo -svg $*.pdf
	

