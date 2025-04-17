checks:
	#no global scope
	#main program
	#each function has documentation
	flake8

clean:
	rm -rf */*/*/__pycache__

gpush:
	git add .
	git commit -m ex06
	git push