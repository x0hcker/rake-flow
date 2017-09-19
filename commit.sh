#!/bin/bash


python setup.py sdist

<<<<<<< HEAD
twine upload dist/rake-flow-{$1}.tar.gz
=======



twine upload dist/rake-flow-$1.tar.gz
>>>>>>> e8d9953a132dc7d50a5837db2b86f5edf6333951

git add .

git commit -m "update {$1}"

git push -u origin master
