FROM ubuntu:20.04

# Dependencies
RUN apt-get update && \
  DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
    texlive-xetex texlive-fonts-extra texlive-latex-extra \
    texlive-fonts-recommended texlive-plain-generic \
    lmodern latexmk python3-pygments

WORKDIR /source
ENTRYPOINT ./make.sh
