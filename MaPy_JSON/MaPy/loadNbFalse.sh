#!/bin/sh
for f in $(ls -t *.zip);\
do
	echo "============== $f ==============";
	unzip -oq $f;
	python3.11 nbFalse.py `basename $f .zip`/solutions_MaPy.txt  `basename $f .zip`/mapping_Neo4j_wikidata.json
	rm -rf  `basename $f .zip`
done;
