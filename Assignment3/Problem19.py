

def probeAlignmentScore ( alignmentMatrix , i , j):
    if (( i < 0 ) and (j < 0)):
        return 0
    elif (( i < 0 ) and (j >= 0)):
        return (j+1)*1
    elif (( i >= 0 ) and (j < 0)):
        return (i+1)*1
    else:
        return alignmentMatrix[i][j]

def calculateNumberAlignments(s , t , i , j , numberAlignmentsMatrix , alignmentMatrix , optScore):
    if ((i < 0) and (j < 0)):
        return 1
    elif ((i < 0) and (j >= 0)):
        return 1
    elif ((i >= 0) and (j < 0)):
        return 1
    elif ( numberAlignmentsMatrix[i][j] != -1 ):
        return numberAlignmentsMatrix[i][j]
    else:
        a = s[i]
        b = t[j]
        totalAlignments = 0

    if (optScore - getScore(a, b) == probeAlignmentScore(alignmentMatrix, i - 1, j - 1)):
        totalAlignments = (totalAlignments + calculateNumberAlignments(s, t, i - 1, j - 1,numberAlignmentsMatrix, alignmentMatrix,optScore - getScore(a, b))) % 134217727
    if (optScore - 1 == probeAlignmentScore(alignmentMatrix, i - 1, j)):
        totalAlignments = (totalAlignments + calculateNumberAlignments(s, t, i - 1, j, numberAlignmentsMatrix,alignmentMatrix, optScore - 1)) % 134217727
    if (optScore - 1 == probeAlignmentScore(alignmentMatrix, i, j - 1)):
        totalAlignments = (totalAlignments + calculateNumberAlignments(s, t, i, j - 1, numberAlignmentsMatrix,alignmentMatrix, optScore - 1)) % 134217727
    numberAlignmentsMatrix[i][j] = totalAlignments
    return totalAlignments

def calculateAlignment(s, t, i, j, alignmentMatrix):
    #print (str(i) + " " + str(j))
    if ((i < 0) and (j < 0)):
        return 0
    elif ((i < 0) and (j >= 0)):
        return (j+1)*1
    elif ((i >= 0) and (j < 0)):
        return (i+1)*1
    elif (alignmentMatrix[i][j] != -1):
        return alignmentMatrix[i][j]
    else:
        a = s[i]
        b = t[j]
        matchOrMismatch = getScore(a, b) + calculateAlignment(s, t, i - 1, j - 1, alignmentMatrix)
        insertion = 1 + calculateAlignment(s, t, i - 1, j, alignmentMatrix)
        deletion = 1 + calculateAlignment(s, t, i, j - 1, alignmentMatrix)
        alignmentMatrix[i][j] = min(matchOrMismatch, min(insertion, deletion))
        return alignmentMatrix[i][j]

def getScore(a,b):
    if a == b :
        return 0
    else:
        return 1

def main():
    inputFile = open('C:/Users/Dhiva/Desktop/input.txt', 'r')
    outputFile = open('C:/Users/Dhiva/Desktop/output.txt', 'w+')
    strings = inputFile.read().split("\n")
    pos = 1
    for string in strings[1:]:
        pos += 1
        if string.find('>') == 0:
            break
    string1= ""
    string2 = ""
    for string in strings[1:pos-1]:
        string1 += string
    for string in strings[pos:len(strings)]:
        string2 += string
    alignmentMatrix = [[-1 for i in range(len(string2))] for j in range(len(string1))]
    numberAlignmentsMatrix = [[-1 for i in range(len(string2))] for j in range(len(string1))]
    optScore = calculateAlignment(string1, string2, len(string1) - 1, len(string2) - 1, alignmentMatrix)
    totalAlignments = calculateNumberAlignments(string1, string2, len(string1) - 1, len(string2) - 1, numberAlignmentsMatrix,alignmentMatrix, optScore)
    print (totalAlignments)

if __name__ == "__main__":
    main()