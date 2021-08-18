#The first argument has to be the directory created by the zip file
lpr=$1
#The second argument has to be the zip file
zip=$2

cp labeler.py $lpr
cd $lpr
python labeler.py --path _annotations.json

#synchronization of files with repair in case of duplicates.
rsync -ab --suffix ~.txt -P images/ ../images/
rsync -ab --suffix ~.txt -P labels/ ../labels/

cd ..
rm -r $lpr
rm $zip

echo "num images: "
ls -l images/ | wc -l
echo "num labels: "
ls -l labels/ | wc -l
