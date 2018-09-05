def main():
    outputFile = open('C:/Users/Dhiva/Desktop/output.txt','w+')
    inputFile = open('C:/Users/Dhiva/Desktop/rosalind_ba1d.txt', 'r')
    refStr = inputFile.readline().strip()
    string = inputFile.readline().strip()
    print (refStr , string)
    refStrLen = len(refStr)
    for i in range(0, len(string) - refStrLen):
        if string[i:i+refStrLen] == refStr:
            outputFile.write(str(i)+" ")
            print(str(i)+" ")
    inputFile.close()
    outputFile.close()

if __name__ == "__main__":
    main()