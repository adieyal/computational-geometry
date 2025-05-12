LATEXMK=latexmk
LATEX_OPTS=-pdf -interaction=nonstopmode -halt-on-error -file-line-error -shell-escape
OUTDIR=build
OUTFORMAT=pdf
MAIN=latex/main.tex

clean:
	find . -type f \( -name "*.aux" -o -name "*.log" -o -name "*.out" -o -name "*.toc" -o -name "*.pdf" -o -name "*.bbl" -o -name "*.blg" -o -name "*.lof" -o -name "*.lot" -o -name "*.fls" -o -name "*.fdb_latexmk" -o -name "*.synctex.gz" \) -delete

all: 
	cd latex && $(LATEXMK) $(LATEX_OPTS) -output-directory=../$(OUTDIR) -output-format=$(OUTFORMAT) main.tex

watch:
	cd latex && $(LATEXMK) $(LATEX_OPTS) -output-directory=../$(OUTDIR) -output-format=$(OUTFORMAT) main.tex

pdf: all
