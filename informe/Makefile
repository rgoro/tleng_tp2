MAIN = main.tex
TEX = $(MAIN)
PDF = Informe_TP2.pdf
CLEAN = *.aux *.log $(PDF)

$(PDF): $(TEX)
	pdflatex $(MAIN)
	pdflatex $(MAIN)
	mv main.pdf $(PDF)

clean:
	rm $(CLEAN)
