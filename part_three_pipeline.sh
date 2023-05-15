#!/bin/sh

# step1
echo "Running step1.py"

python3 step1.py

# #step 2
echo "Running step2.py"

python3 step2.py

echo "NCVOG_Final.fa made"

#step 3: align

mafft-linsi NCVOG_Final.fa > mafft_NCVOG.algn

#step 4: filter

trimal -in  mafft_NCVOG.algn -out trimal_mafft_NCVOG.algn -gappyout

#step 5: remove duplicate values

python3 remove_dup.py

#step 6: make tree

sudo chmod -R 777 /home/henrik

FastTree "trimal_mafft_NCVOG_unique.algn" > NCVOG.tree

#step 7: save plot tree

plottree NCVOG.tree -o NCVOG_tree_image.png