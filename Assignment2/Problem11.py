def main():
    inputFile = open('C:/Users/Dhiva/Desktop/input.txt', 'r')
    outputFile = open('C:/Users/Dhiva/Desktop/output.txt', 'w+')
    string = inputFile.read()
    patterns = string.split()
    trieConstruction(patterns)
    print(patterns)

def trieConstruction(patterns):
    trie = []
    nodes = dict()
    nodeNum = 0
    for pattern in patterns:
        currentNode = 0
        for i in pattern:
            print (str(currentNode) + " " + i)
            if currentNode in nodes:
                #for j in nodes[currentNode]:
                #    print (j)
                if nodes[currentNode][0][1] == i:
                    currentNode = nodes[currentNode][0][0]
                    print ("currentNode = " + str(currentNode))
                else:
                    nodeNum += 1
                    tempList = nodes[currentNode]
                    tempList.append((nodeNum, i))
                    nodes[currentNode] = tempList
                    print (tempList)
                    print (nodes[currentNode])
                    currentNode = nodeNum
                    print(nodes)
            else:
                nodeNum += 1
                nodes[currentNode] = [(nodeNum, i)]
                currentNode = nodeNum
                print (nodes)
    print (nodes)



if __name__ == "__main__":
    main()