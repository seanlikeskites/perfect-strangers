all: submatrix_before.svg submatrix_after.svg submatrix_zero.svg submatrix_one.svg submatrix_two.svg

export TEXINPUTS := ../:${TEXINPUTS}

%.svg: %.tex ../colours.tex
	pdflatex $<
	pdftocairo -svg $*.pdf
	

