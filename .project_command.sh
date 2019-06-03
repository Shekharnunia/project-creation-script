#!/bin/bash
function create() {
	cd /home/shekhar/Desktop/Development/
	mkdir -p $1
	cd $1
	python /home/shekhar/Desktop/Development/project-creation-script/project.py $1
	git init
	git remote add origin https://github.com/Shekharnunia/$1.git 
	touch README.md
	git add .
	git commit -m "inital commit"

}
