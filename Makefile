LATEXMK=latexmk
LATEX_OPTS=-verbose -interaction=nonstopmode -halt-on-error -file-line-error -shell-escape -bibtex-
OUTDIR=../build
OUTFORMAT=pdf
PROJECT_DIR=./segment-trees/
MAIN=segment-trees.tex
BIBFILE=$(PROJECT_DIR)/sample-handout.bib


clean:
	find . -type f \( -name "*.aux" -o -name "*.log" -o -name "*.out" -o -name "*.toc" -o -name "main.pdf" -o -name "*.bbl" -o -name "*.blg" -o -name "*.lof" -o -name "*.lot" -o -name "*.fls" -o -name "*.fdb_latexmk" -o -name "*.synctex.gz" -o -name "*.idx" -o -name "*.ilg" -o -name "*.ind" \) -delete

all:
	cd $(PROJECT_DIR) && $(LATEXMK) $(LATEX_OPTS) -output-directory=$(OUTDIR) -output-format=$(OUTFORMAT) $(MAIN)

watch:
	cd $(PROJECT_DIR) && $(LATEXMK) $(LATEX_OPTS) -output-directory=$(OUTDIR) -output-format=$(OUTFORMAT) $(MAIN)

pdf: all
