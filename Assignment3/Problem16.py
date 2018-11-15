import sys

path = []

def main():
    inputFile = open('C:/Users/Dhiva/Desktop/input.txt', 'r')
    outputFile = open('C:/Users/Dhiva/Desktop/output.txt', 'w+')
    string = inputFile.read()
    edgesDict,start,end = hashBuilder(string)
    print (edgesDict)
    print (start)
    print (end)
    vertices = vertCalc(edgesDict)

    #edgesDict = missingFix(edgesDict)
    visited = [False] * (vertices+1)
    stack = []
    dist = [-sys.maxsize -1] * (vertices + 1)
    dist[int(start)] = 0
    for i in range(vertices):
        if visited[i] == False:
            topologicalSortUtil(str(i), visited, stack,edgesDict)
    print (stack)
    print (dist)
    while (len(stack) != 0):
        u = stack.pop(0)
        if dist[int(u) != -sys.maxsize -1]:
            if u in edgesDict:
                for i in edgesDict[u]:
                    if ( dist[int(i[0])] < dist[int(u)] + int(i[1]) ):
                        dist[int(i[0])] = dist[int(u)] + int(i[1])
    u  = (start,'0')
    temp = [start]
    sum = 0
    path = longPath(sum,temp,u,edgesDict,dist[int(end)])
    print (dist[int(end)])

def longPath(sum,temp,u,edgesDict,target):
    sum += int(u[1])
    if (sum == target):
        outputFile = open('C:/Users/Dhiva/Desktop/output.txt', 'w+')
        outputFile.write(str(target)+"\n")
        for k in temp:
            outputFile.write(k+"->")
    if u[0] in edgesDict:
        for i in edgesDict[u[0]]:
            temp.append(i[0])
            longPath(sum,temp,i,edgesDict,target)



def topologicalSortUtil(v, visited, stack,edgesDict):
    visited[int(v)] = True
    if v in edgesDict:
        for i in edgesDict[v]:
            if visited[int(i[0])] == False:
                topologicalSortUtil(i[0], visited, stack,edgesDict)
    stack.insert(0,v)

def vertCalc(edgesDict):
    max = 0
    for key,value in edgesDict.items():
        if int(key) > max:
            max = int(key)
        for node in value:
            if int(node[0]) > max:
                max = int(node[0])
    return max

def hashBuilder(string):
    edgesDict = dict()
    edges = string.split('\n')
    # print (edges)
    start = edges[0].strip()
    end = edges[1].strip()
    for edge in edges[2:]:
        nodes = edge.split('->')
        if nodes[0].strip() in edgesDict:
            edgesDict[nodes[0].strip()].append(tuple(i.strip() for i in "".join(nodes[1:]).split(':')))
        else:
            edgesDict[nodes[0].strip()] = []
            edgesDict[nodes[0].strip()].append(tuple(i.strip() for i in "".join(nodes[1:]).split(':')))
    return edgesDict,start,end

if __name__ == "__main__":
    main()