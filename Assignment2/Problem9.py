# Python

def main():
    inputFile = open('C:/Users/Dhiva/Desktop/rosalind_ba3m.txt', 'r')
    outputFile = open('C:/Users/Dhiva/Desktop/output.txt', 'w+')
    string = inputFile.read()
    edgesDict = hashBuilder(string)
    inDict = dict()
    outDict = dict()
    degreeCount(edgesDict, inDict, outDict)
    paths = nonBranchpaths(edgesDict, inDict, outDict)
    icPaths = isolatedCycle(edgesDict, inDict, outDict)
    paths.extend(icPaths)
    for path in paths:
        len_path = len(path)
        for i in range(len_path):
            outputFile.write(path[i])
            if i != len_path-1:
                outputFile.write(" -> ")
        outputFile.write("\n")

def isolatedCycle(edgesDict, inDict, outDict):
    paths = []
    notVisited  = list(edgesDict.keys())
    for node in notVisited:
        print(notVisited)
        tempList = [node]
        notVisited.remove(node)
        while (isOneToOne(tempList[-1],inDict,outDict)):
            tempList.append(edgesDict[tempList[-1]][0])
            print (tempList[-1])
            if tempList[-1] in notVisited:
                notVisited.remove(tempList[-1])
            if(tempList[0] == tempList[-1]):
                paths.append(tempList)
                break
    return paths

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


def isOneToOne(node, inDict, outDict):
    if (node in inDict and node in outDict):
        if inDict[node] == 1 and outDict[node] == 1:
            return True
    return False


def nonBranchpaths(graph, inDict, outDict):
    paths = []
    for node in graph:
        if not (isOneToOne(node, inDict, outDict)):
            if outDict[node] > 0:
                for outEdge in graph[node]:
                    tempList = []
                    w = str(outEdge)
                    tempList.append(node)
                    tempList.append(w)
                    while ( isOneToOne(w,inDict,outDict) ):
                        w = (graph[w][0])
                        tempList.append(w)
                    paths.append(tempList)
    return paths

def hashBuilder(string):
    edgesDict = dict()
    edges = string.split('\n')
    # print (edges)
    for edge in edges:
        nodes = edge.split('->')
        edgesDict[nodes[0].strip()] = [i.strip() for i in "".join(nodes[1:]).split(',')]
    return edgesDict

if __name__ == "__main__":
    main()
