all: initial.svg one_shift.svg two_shifts.svg three_shifts.svg four_shifts.svg submatrix_before.svg submatrix_after.svg submatrix_zero.svg submatrix_one.svg submatrix_two.svg transpose_and_shift.svg

%.svg: %.tex colours.tex
	pdflatex $<
	pdftocairo -svg $*.pdf
	

