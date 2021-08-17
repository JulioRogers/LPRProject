# Rename all *.txt to *.text

idx=0
for f in *.txt~.txt; do 
    mv -- "$f" "${f%.txt~.txt}_{$idx}.txt"
    idx=$(($idx+1))
done
