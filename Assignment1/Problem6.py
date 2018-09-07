def main():
    DNA_CODON_TABLE = {
        'TTT': 'F', 'CTT': 'L', 'ATT': 'I', 'GTT': 'V',
        'TTC': 'F', 'CTC': 'L', 'ATC': 'I', 'GTC': 'V',
        'TTA': 'L', 'CTA': 'L', 'ATA': 'I', 'GTA': 'V',
        'TTG': 'L', 'CTG': 'L', 'ATG': 'M', 'GTG': 'V',
        'TCT': 'S', 'CCT': 'P', 'ACT': 'T', 'GCT': 'A',
        'TCC': 'S', 'CCC': 'P', 'ACC': 'T', 'GCC': 'A',
        'TCA': 'S', 'CCA': 'P', 'ACA': 'T', 'GCA': 'A',
        'TCG': 'S', 'CCG': 'P', 'ACG': 'T', 'GCG': 'A',
        'TAT': 'Y', 'CAT': 'H', 'AAT': 'N', 'GAT': 'D',
        'TAC': 'Y', 'CAC': 'H', 'AAC': 'N', 'GAC': 'D',
        'TAA': '', 'CAA': 'Q', 'AAA': 'K', 'GAA': 'E',
        'TAG': '', 'CAG': 'Q', 'AAG': 'K', 'GAG': 'E',
        'TGT': 'C', 'CGT': 'R', 'AGT': 'S', 'GGT': 'G',
        'TGC': 'C', 'CGC': 'R', 'AGC': 'S', 'GGC': 'G',
        'TGA': '', 'CGA': 'R', 'AGA': 'R', 'GGA': 'G',
        'TGG': 'W', 'CGG': 'R', 'AGG': 'R', 'GGG': 'G'
    }
    protein = ''
    outputFile = open('C:/Users/Dhiva/Desktop/output.txt','w+')
    inputFile = open('C:/Users/Dhiva/Desktop/rosalind_splc.txt', 'r')
    string = inputFile.read().strip()
    lines =  string.split()
    print (string)
    print (lines)
    exon = lines[1]
    for i in range(3 , len(lines),2):
        exon = exon.replace(lines[i],"")
    for i in range(0, len(exon), 3):
        if(exon[i:i+3] in DNA_CODON_TABLE):
            if DNA_CODON_TABLE[exon[i:i+3]] != "":
                protein += DNA_CODON_TABLE[exon[i:i+3]]
            else:
                break
    print (protein)
    outputFile.write(protein)
    inputFile.close()
    outputFile.close()

if __name__ == "__main__":
    main()