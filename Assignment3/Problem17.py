import sys

def edit_distance(string1, string2):
    cost_matrix = [1, 1, 1, 0]
    matrix = [[None for i in range(len(string2))] for j in range(len(string1))]
    return fill_column(string1, string2, len(string1) - 1, len(string2) - 1, cost_matrix, matrix)

def fill_column(string1, string2, i, j, cost_matrix, matrix):
    if matrix[i][j] != None:
        return matrix[i][j]
    delete_cost = cost_matrix[0]
    insert_cost = cost_matrix[1]
    replace_cost = cost_matrix[2]
    same_cost = cost_matrix[3]
    if i == 0 and j == 0:
        if string1[i] == string2[j]:
            order3 = same_cost
        else:
            order3 = replace_cost
        matrix[i][j] = order3
        return order3
    elif i == 0 and j >= 1:
        order2 = insert_cost + fill_column(string1, string2, i, j - 1, cost_matrix, matrix)
        matrix[i][j] = order2
        return order2
    elif i >= 1 and j == 0:
        order1 = delete_cost + fill_column(string1, string2, i - 1, j, cost_matrix, matrix)
        matrix[i][j] = order1
        return order1
    else:
        order1 = delete_cost + fill_column(string1, string2, i - 1, j, cost_matrix, matrix)
        order2 = insert_cost + fill_column(string1, string2, i, j - 1, cost_matrix, matrix)
        if string1[i] == string2[j]:
            order3 = same_cost + fill_column(string1, string2, i - 1, j - 1, cost_matrix, matrix)
        else:
            order3 = replace_cost + fill_column(string1, string2, i - 1, j - 1, cost_matrix, matrix)
        order = min(order1, order2, order3)
        matrix[i][j] = order
        return order


def main():
    inputFile = open('C:/Users/Dhiva/Desktop/input.txt', 'r')
    outputFile = open('C:/Users/Dhiva/Desktop/output.txt', 'w+')
    strings = inputFile.read().split("\n")
    print (strings)
    pos = 1
    for string in strings[1:]:
        pos += 1
        if string.find('>') == 0:
            break
    print (pos)
    string1= ""
    string2 = ""
    for string in strings[1:pos-1]:
        string1 += string
    for string in strings[pos:len(strings)]:
        string2 += string
    print (string1)
    print (string2)
    sys.setrecursionlimit(2500)
    temp = edit_distance(string1, string2)
    print (temp)
    #print (sys.getrecursionlimit())
    
if __name__ == "__main__":
    main()