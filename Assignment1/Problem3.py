protein = {}

def main():
    outputFile = open('C:/Users/Dhiva/Desktop/output.txt','w+')
    inputFile = open('C:/Users/Dhiva/Desktop/rosalind_kmer.txt', 'r')
    string = inputFile.read().replace("\n","")
    for x in range(0,len(string)-3):
        #print(string[x:x+4])
        if string[x:x+4] in protein:
            protein[string[x:x+4]] = protein[string[x:x+4]] + 1
    for x in protein:
        outputFile.write(str(protein[x])+" ")
        print (protein[x])
    inputFile.close()
    outputFile.close()

def build_kmer():
    s = "ACGT"
    for i in s:
        for j in s:
            for k in s:
                for l in s:
                    protein[i+j+k+l] = 0

if __name__ == "__main__":
    build_kmer()
    main()