.PHONY: theme mvrk site
default: site

theme:
	git pull
	git submodule update --init --recursive
	cd Galileo && git pull origin latest --rebase
	git add .
	git commit -m "Update theme"
	git push

mvrk:
	git pull
	git submodule update --init --recursive
	cd Maverick && git pull origin master --rebase
	git add .
	git commit -m "Update Maverick"
	git push

site:
	git pull
	git add .
	git commit -m "Update site ${msg}"
	git push
