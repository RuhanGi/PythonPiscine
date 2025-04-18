checks:
	#no global scope
	#main program
	#each function has documentation
	flake8

clean:
	rm -rf */*/__pycache__
	rm -rf */*/*.pyc
	find . -name .DS_Store -delete

gpush: clean
	git add .
	git commit -m draftfinish
	git push

f:
	/Users/mgoltay/Library/Python/3.12/bin/flake8
