all: ls1.svg ls2.svg ls3.svg overlayed_squares.svg

export TEXINPUTS := ../:${TEXINPUTS}

%.svg: %.tex
	pdflatex $<
	pdftocairo -svg $*.pdf
	

