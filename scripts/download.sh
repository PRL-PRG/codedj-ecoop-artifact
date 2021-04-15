#!/bin/bash

mkdir -p toy-dataset/
parasite/target/release/parasite --datastore toy-dataset add toy-dataset-repositories.csv
echo -e "loadall\nupdateall" | parasite/target/release/parasite --datastore toy-dataset -ght ghtokens.csv -n 8 --interactive
#echo "updateall" | parasite/target/release/parasite --datastore toy-dataset -ght ghtokens.csv -n 8 --interactive
#parasite/target/release/parasite --datastore toy-dataset -ght ghtokens.csv -n 8 --interactive