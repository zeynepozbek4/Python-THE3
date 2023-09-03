def pattern_search(x,L):

    def rotate_matrix(lst):
        turned = [[lst[x][y] for x in range(len(lst))] for y in range(0, len(lst[0]))]
        new_matrix = []
        for e in turned:
            p = "".join(e)[::-1]
            new_matrix.append(p)
        return new_matrix

    angle = 0
    for i in range(len(L[0])-len(x[0])+1):
        for j in range(len(L)-len(x)+1):
            count = 0
            for k in range(len(x[0])):
                for l in range(len(x)):
                    if x[l][k]==L[j+l][i+k]:
                        count += 1
                    else:
                        break
            if count == len(x[0]) * len(x):
                return (j, i, angle)

    x = rotate_matrix(x)
    angle = 90
    for i in range(len(L[0])-len(x[0])+1):
        for j in range(len(L)-len(x)+1):
            count = 0
            for k in range(len(x[0])):
                for l in range(len(x)):
                    if x[l][k]==L[j+l][i+k]:
                        count += 1
                    else:
                        break
            if count == len(x[0]) * len(x):
                return (j, i, angle)

    x = rotate_matrix(x)
    angle = 180
    for i in range(len(L[0]) - len(x[0]) + 1):
        for j in range(len(L) - len(x) + 1):
            count = 0
            for k in range(len(x[0])):
                for l in range(len(x)):
                    if x[l][k] == L[j + l][i + k]:
                        count += 1
                    else:
                        break
            if count == len(x[0]) * len(x):
                return (j, i, angle)

    x = rotate_matrix(x)
    angle = 270
    for i in range(len(L[0]) - len(x[0]) + 1):
        for j in range(len(L) - len(x) + 1):
            count = 0
            for k in range(len(x[0])):
                for l in range(len(x)):
                    if x[l][k] == L[j + l][i + k]:
                        count += 1
                    else:
                        break
            if count == len(x[0]) * len(x):
                return (j, i, angle)
    return False

