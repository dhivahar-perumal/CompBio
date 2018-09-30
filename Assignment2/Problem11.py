def main():
    inputFile = open('C:/Users/Dhiva/Desktop/rosalind_ba9a.txt', 'r')
    inputFile = open('C:/Users/Dhiva/Desktop/rosalind_ba9a.txt', 'r')
    outputFile = open('C:/Users/Dhiva/Desktop/output.txt', 'w+')
    string = inputFile.read()
    patterns = string.split()
    nodes = trieConstruction(patterns)
    for node in nodes:
        for i in nodes[node]:
            outputFile.write(str(node)+"->"+str(i[0])+":"+i[1]+"\n")
    print (nodes)

def trieConstruction(patterns):
    nodes = dict()
    nodeNum = 0
    for pattern in patterns:
        currentNode = 0
        for i in pattern:
            if currentNode in nodes:
                for j in nodes[currentNode]:
                    if j[1] == i:
                        break
                if j[1] == i:
                    currentNode = j[0]
                else:
                    nodeNum += 1
                    tempList = nodes[currentNode]
                    tempList.append((nodeNum, i))
                    nodes[currentNode] = tempList
                    currentNode = nodeNum
            else:
                nodeNum += 1
                nodes[currentNode] = [(nodeNum, i)]
                currentNode = nodeNum
    return nodes


if __name__ == "__main__":
    main()