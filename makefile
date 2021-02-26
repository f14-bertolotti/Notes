
clean:
	rm main.log main.aux main.out main.toc 

plots:
	python3 ./GeneralizedLinearModels/figs/Bernulli-plot.py

tex:
	pdflatex main.tex


all: plots tex tex clean

