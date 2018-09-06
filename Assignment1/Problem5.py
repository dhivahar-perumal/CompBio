def main():
    kmer = {}
    maxVal = 0
    outputFile = open('C:/Users/Dhiva/Desktop/output.txt','w+')
    inputFile = open('C:/Users/Dhiva/Desktop/rosalind_ba1b.txt', 'r')
    string = inputFile.readline().strip()
    kmerVal = int(inputFile.readline())
    print (kmerVal , string)
    for i in range(0, len(string) - kmerVal):
        if string[i:i+kmerVal] in kmer:
            kmer[string[i:i+kmerVal]] = kmer[string[i:i+kmerVal]] + 1
        else:
            kmer[string[i:i + kmerVal]] = 0
    for p in kmer.items():
       if(p[1] > maxVal):
           maxVal = p[1]
    print (kmer , "\n" , str(maxVal))
    for p in kmer.items():
        if p[1] == maxVal:
            outputFile.write(p[0] + " ")
            print (p[0])
    inputFile.close()
    outputFile.close()

if __name__ == "__main__":
    main()