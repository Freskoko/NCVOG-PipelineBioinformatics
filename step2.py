import re

with open("genomes.txt","r") as f:
    lines = f.readlines()
    linesLookingFor = [(i.strip()) for i in lines]

print(linesLookingFor)

name_and_seq = []

with open("NCVOG.fa","r") as f:

    lines2 = f.readlines()
    lines2 = "".join(lines2)
    lines2 = lines2.strip()
    lines2 = lines2.split(">")

    for i in lines2:
        
        try:
      
            name,seq = (i.split("\n",1))

            # -------------- find num code --------------
   
            pattern = r'(?<=\|)[^|]+'
            
            text_between_brackets_name = re.findall(pattern, name)

            name_between = text_between_brackets_name[0].replace(" ","_")

            # -------------- find virus name --------------

            pattern2 = r'\[(.*?)\]'
            
            virus_Name = re.findall(pattern2, name)

            virus_Name = virus_Name[0].replace(" ","_")

            # -------------- put name and seq in a list --------------

            if name_between in linesLookingFor:
                name_and_seq.append(f">{virus_Name}\n{seq}")

        except Exception as e:
            print(e)

with open("NCVOG_Final.fa","w") as f:
    for i in name_and_seq:
        f.write(i)




