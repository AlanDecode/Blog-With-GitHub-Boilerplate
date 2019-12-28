::Update Maverick and Commit Changes

git pull

git submodule update --init --recursive
cd Maverick
git pull origin master --rebase

cd ..
git add .
git commit -m "Update Maverick"
git push

pause
