def main():
    path = 'C:/Users/Dhiva/Desktop/rosalind_dna.txt'
    protein = {
        "A" : 0,
        "C": 0,
        "G": 0,
        "T": 0,
    }
    inputFile = open(path, 'r')
    str = inputFile.read()
    print (str)
    for c in str:
        if c in protein:
            protein[c] = protein[c] + 1
    print (protein["A"],protein["C"],protein["G"],protein["T"])

if __name__ == "__main__":
    main()
