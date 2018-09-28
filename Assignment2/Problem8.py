#Python

def main():
    preList = []
    posList = []
    resultSet = set()
    inputFile = open('C:/Users/Dhiva/Desktop/rosalind_dbru.txt', 'r')
    outputFile = open('C:/Users/Dhiva/Desktop/output.txt', 'w+')
    tempString = ""

    string = inputFile.read().strip()
    lines = string.split()
    for mer in lines:
        temp = reverseComplement(mer)
        tempString = "(" + mer[:-1] + "," + mer[1:] + ")"
        resultSet.add(tempString)
        tempString = "(" + temp[:-1] + "," + temp[1:] + ")"
        resultSet.add(tempString)
    resultSet = sorted(resultSet)
    for i in resultSet:
        print(str(i))
        outputFile.write( str(i)+ "\n")


def reverseComplement(input):
    result = ""
    complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
    for ind, val in enumerate(input):
        if val in complement:
            result += complement[val]
    return result[::-1]


if __name__ == "__main__":
    main()
