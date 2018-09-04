def main():
    outputFile = open('C:/Users/Dhiva/Desktop/output.txt','w+')
    inputFile = open('C:/Users/Dhiva/Desktop/rosalind_rna.txt', 'r')
    str = inputFile.read()
    for c in str:
        if c == "T":
            outputFile.write("U")
        else:
            outputFile.write(c)
    inputFile.close()
    outputFile.close()

if __name__ == "__main__":
    main()