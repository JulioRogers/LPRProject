# Rename all *.txt~.txt to namefile(idx).txt where idx is a iterator.

idx=0
for f in *.txt~.txt; do 
    mv -- "$f" "${f%.txt~.txt}_{$idx}.txt"
    idx=$(($idx+1))
done
