all: finite_affine_plane.svg

%.svg: %.tex
	pdflatex $<
	pdftocairo -svg $*.pdf
	

