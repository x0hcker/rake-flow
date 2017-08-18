#!/bin/bash


python setup.py sdist




twine upload dist/rake-flow-$1.tar.gz

git add .

git commit -m "update {$1}"

git push -u origin master
