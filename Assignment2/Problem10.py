def main():
    inDict = {}
    outDict = {}
    inputFile = open('C:/Users/Dhiva/Documents/Assignment Comp Bio/rosalind_ba3g.txt', 'r')
    outputFile = open('C:/Users/Dhiva/Documents/Assignment Comp Bio/output.txt', 'w+')
    string = inputFile.read()
    edgesDict = hashBuilder(string)
    degreeCount(edgesDict,inDict,outDict)
    startEdge = startEdgeFinder(edgesDict,inDict,outDict)
    eulerPath = eulerPathBuilder(edgesDict,startEdge,outDict)
    print (edgesDict)
    print (inDict)
    print (outDict)
    for i in eulerPath:
        outputFile.write(str(i) + "->" )

def startEdgeFinder(edgesDict, inDict, outDict):
    global edge
    oddVertices = []
    for edge in edgesDict:
        if (outDict[edge] - inDict[edge] ) == 1:
            oddVertices.append(edge)
    if len(oddVertices) != 0:
        return oddVertices.pop()
    else:
        return '0'

def eulerPathBuilder(edgesDict,startEdge,outDict):
    eulerPath = []
    curPath = []
    curPath.append(startEdge)
    curVert = startEdge
    while (len(curPath) != 0):
        if ((outDict[curVert])!=0):
            curPath.append(curVert)
            nextVert = edgesDict[curVert].pop()
            outDict[curVert] -= 1
            #curPath.append(nextVert)
            curVert = nextVert

        else:
            eulerPath.append(curVert)
            curVert = curPath.pop()
    eulerPath.reverse()
    print (eulerPath)
    print(curPath)
    return eulerPath


def hashBuilder(string):
    edgesDict = dict()
    edges = string.split('\n')
    # print (edges)
    for edge in edges:
        nodes = edge.split('->')
        edgesDict[nodes[0].strip()] = [i.strip() for i in "".join(nodes[1:]).split(',')]
    return edgesDict

def degreeCount(edgesDict, inDict, outDict):
    for key, val in edgesDict.items():
        outDict[key] = len(val)
        #print(str( key ) + " = " + str(len(val)) )
        if key not in inDict:
            inDict[key] = 0
    for val in edgesDict.values():
        for i in val:
            if i in inDict:
                inDict[i] += 1
            else:
                inDict[i] = 1
            if i not in outDict:
                outDict[i] = 0

if __name__ == "__main__":
    main()