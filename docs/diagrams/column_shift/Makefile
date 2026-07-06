all: initial.svg one_shift.svg two_shifts.svg three_shifts.svg four_shifts.svg transpose_and_shift.svg submatrix_one.svg

export TEXINPUTS := ../:${TEXINPUTS}

%.svg: %.tex ../colours.tex
	pdflatex $<
	pdftocairo -svg $*.pdf
	

