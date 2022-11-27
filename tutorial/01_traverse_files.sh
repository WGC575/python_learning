#!bin/bash/

names=$(ls .)
echo $names
for dir in $names
do
    echo $dir
    mkdir ${dir%.py}
done