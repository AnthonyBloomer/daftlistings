if [ $# -eq 0 ]
  then
    echo "No commit message supplied"
	exit 0
fi
mkdocs build
mv -v site ~/
git checkout gh-pages
rm -rf *
cp -a ~/site/ .
git add .
git commit -m "$1"
git push
rm -rf ~/site
git checkout master
virtualenv env
source env/bin/activate
pip install -r requirements.txt
