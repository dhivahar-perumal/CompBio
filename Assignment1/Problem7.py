def main():
    outputFile = open('C:/Users/Dhiva/Desktop/output.txt','w+')
    inputFile = open('C:/Users/Dhiva/Desktop/rosalind_ba6e.txt', 'r')
    kmer = {}
    kmerVal = int(inputFile.readline().strip())
    string1 = inputFile.readline().strip()
    string2 = inputFile.readline().strip()
    #print (kmerVal,string1,string2)
    for i in range(0,len(string1)-kmerVal+1):
        if string1[i:i+kmerVal] not in kmer:
            kmer[string1[i:i+kmerVal]] = [i]
            kmer[reverseComplement(string1[i:i + kmerVal])] = [i]
        else:
            kmer[string1[i:i + kmerVal]].append(i)
            kmer[reverseComplement(string1[i:i + kmerVal])].append(i)
    for i in range(0,len(string2)-kmerVal+1):
        if (string2[i:i+kmerVal] in kmer):
            for j in kmer[string2[i:i+kmerVal]]:
                #print ((j,i))
                outputFile.write(str((j,i))+"\n")

    #print (kmer)
    inputFile.close()
    outputFile.close()

def reverseComplement(input):
    result = ""
    complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
    for ind,val in enumerate(input):
        if val in complement:
            result += complement[val]
    return (result[::-1])


if __name__ == "__main__":
    reverseComplement("ATC")
    main()