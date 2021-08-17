lpr=$1
zip=$2
cp labeler.py $lpr
cd $lpr
python labeler.py --path _annotations.json
rsync -ab --suffix ~.txt -P images/ ../images/
rsync -ab --suffix ~.txt -P labels/ ../labels/
cd ..
rm -r $lpr
rm $zip
echo "num images: "
ls -l images/ | wc -l
echo "num labels: "
ls -l labels/ | wc -l
