#!/bin/bash

git clone https://github.com/PRL-PRG/codedj-parasite.git parasite
cd parasite
cargo build --release
cd ..

git clone https://github.com/PRL-PRG/djanco.git 
cd djanco 
cargo build --release
cd ..