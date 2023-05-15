import pandas as pd 

# //CHANGE THIS TO CHANGE NCVOG NUMBER
NCVOG_NUMBER = "NCVOG0001"

filein = pd.read_csv("NCVOG.csv")

genomes = []

for index,id in filein.iloc[:,6].iteritems():
    if id == NCVOG_NUMBER:

        #adds the element at the same colum as id, but row element 1 to genomes.
        genomes.append(filein.loc[index, filein.columns[0]])

with open("genomes.txt","w") as f:
    for i in genomes:
        f.write(f"{i}\n")