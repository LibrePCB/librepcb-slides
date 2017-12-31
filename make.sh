#!/bin/bash

latexmk -pdf -e '$pdflatex=q/xelatex --shell-escape %O %S/' slides.tex
