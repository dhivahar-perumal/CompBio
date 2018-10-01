#Python

def main():
    inputFile = open('C:/Users/Dhiva/Desktop/rosalind_ba9g.txt', 'r')
    outputFile = open('C:/Users/Dhiva/Desktop/output.txt', 'w+')
    string = inputFile.read().strip()
    sufArr = genSuffixArray(string)
    for pos in sufArr:
        outputFile.write(str(pos)+", ")

def genSuffixArray(string):
    tempList = []
    sufArr = []
    for i in range(len(string)-1,-1,-1):
        tempList.append(string[i:])
    tempList.sort()
    for seq in tempList:
        sufArr.append(string.find(seq))
    return sufArr

if __name__ == "__main__":
    main()
