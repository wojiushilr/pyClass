def bag(n, c, w, v):

    res = [[-1 for j in range(c + 1)] for i in range(n + 1)]
    for j in range(c + 1):
        res[0][j] = 0
    for i in range(1, n + 1):
        for j in range(1, c + 1):
            res[i][j] = res[i - 1][j]
            if j >= w[i - 1] and res[i][j] < res[i - 1][j - w[i - 1]] + v[i - 1]:
                res[i][j] = res[i - 1][j - w[i - 1]] + v[i - 1]
    return res


def show(n, c, w, res):
    print(res[n][c])

if __name__ == '__main__':


    w2 = input().split(",")
    v2 = input().split(",")
    w =[]
    v =[]

    for i in range(len(w2)):
        w.append(int(w2[i]))
        v.append(int(v2[i]))


    map(int,w)
    map(int,v)
    c = int(input())
    n = len(w)
    res = bag(n, c, v, w)
    show(n, c, v, res)
