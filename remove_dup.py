input_file = "trimal_mafft_NCVOG.algn"
output_file = "trimal_mafft_NCVOG_unique.algn"

with open(input_file, "r") as infile, open(output_file, "w") as outfile:
    names = {}
    for line in infile:
        if line.startswith(">"):
            name = line.strip()
            if name in names:
                names[name] += 1
                new_name = f"{name}_{names[name]}"
            else:
                names[name] = 0
                new_name = name
            outfile.write(f"{new_name}\n")
        else:
            outfile.write(line)