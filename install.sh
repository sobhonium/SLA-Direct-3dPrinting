#!/usr/bin/bash

# Download and place UVtools in /tools folder.
cd ./tools
wget https://github.com/sn4k3/UVtools/releases/download/v3.13.1/UVtools_linux-x64_v3.13.1.zip 

mkdir UVtools_linux-x64_v3.13.1
unzip  UVtools_linux-x64_v3.13.1.zip -d UVtools_linux-x64_v3.13.1
cd ..
# install requirements.txt 
