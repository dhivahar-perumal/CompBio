def main():
    inputFile = open('C:/Users/Dhiva/Desktop/rosalind_ba5n.txt', 'r')
    outputFile = open('C:/Users/Dhiva/Desktop/output.txt', 'w+')
    string = inputFile.read()
    edgesDict = hashBuilder(string)
    print (edgesDict)
    vertices = vertCalc(edgesDict)
    #edgesDict = missingFix(edgesDict)
    visited = [False] * (vertices+1)
    stack = []
    for i in range(vertices):
        if visited[i] == False:
            topologicalSortUtil(str(i), visited, stack,edgesDict)
    print (stack)
    for e in stack:
        outputFile.write(e+", ")

def topologicalSortUtil(v, visited, stack,edgesDict):
    visited[int(v)] = True
    print (visited)
    if v in edgesDict:
        print(v)
        for i in edgesDict[v]:
            print ("i=",i)
            if visited[int(i)] == False:
                topologicalSortUtil(i, visited, stack,edgesDict)
    stack.insert(0,v)


def vertCalc(edgesDict):
    max = 0
    for key,value in edgesDict.items():
        if int(key) > max:
            max = int(key)
        for node in value:
            if int(node) > max:
                max = int(node)
    return max

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