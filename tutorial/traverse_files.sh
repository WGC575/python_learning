#!bin/bash/

names=$(ls .)
echo $names
for dir in $names
do
    echo $dir
    mkdir ${dir%.py}
done

# read folder names in ./
names=$(ls ./)

# traverse the folders in ./
for dir in $names
do 
    # read files in folders
    names_py=$(ls ./${dir})
    for dir_py in $names_py

    # move files out from the folder to ./
    do
        echo ${dir}/${dir_py}
        mv -v ${dir}/${dir_py} ${dir_py}
    done
done