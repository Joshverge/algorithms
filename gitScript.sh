#!/bin/bash  
# for cheat sheet: https://devhints.io/bash
# chmod +x script.sh
# ./script.sh arg1 arg2
# varible not found: https://stackoverflow.com/questions/2268104/command-not-found-error-in-bash-variable-assignment

remove="$1"
echo "$remove" 
if [[ -n "$remove" ]] && [[ "$remove" == "add" ]] ; then
	touch TestBed.py
	git add TestBed.py
	git commit -m "adding TestBed.py"
	git push
else
	git rm TestBed.py
	git commit -m "removing TestBed.py"
	git push
fi