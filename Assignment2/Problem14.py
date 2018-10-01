#Python
import re

def main():
    inputFile = open('C:/Users/Dhiva/Desktop/rosalind_ba9h.txt', 'r')
    outputFile = open('C:/Users/Dhiva/Desktop/output.txt', 'w+')
    string = inputFile.read()
    patterns = string.split()
    substringPos = patternMatch(patterns)
    for pos in substringPos:
        outputFile.write(str(pos)+" ")

def patternMatch(patterns):
    refString = patterns[0]
    print(refString)
    posList = []
    tempList = []
    for subString in patterns[1:]:
        print(subString)
        posList = [m.start() for m in re.finditer('(?=' + subString + ')', refString)]
        print(posList)
        tempList.extend(posList)
    tempList.sort()
    print(tempList)
    return tempList

if __name__ == "__main__":
    main()