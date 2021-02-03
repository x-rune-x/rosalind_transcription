def transcribe(t):
    input_file = open(t, "r")
    dna = input_file.read()
    rna = ""
    for nucleotide in dna:
        if nucleotide.upper() == "T":
            rna += "U"
        else:
            rna += nucleotide

    input_file.close()
    return rna


rna_output = transcribe("rosalind_rna.txt")
print(rna_output)
output_file = open("rna_output.txt", "w")
output_file.write(rna_output)
output_file.close()
