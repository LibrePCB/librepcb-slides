#!/bin/bash

DIR=$(dirname "$(readlink -f "$0")")
docker run --rm -it --user `id -u`:`id -g` -v "$DIR:/source" librepcb-slides
