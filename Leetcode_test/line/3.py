global col
global row
global pos_diag
global nag_diag
global count


def output():
    global count
    print(row)
    count += 1


def do_queen(i, n):
    for j in range(0, n):

        if col[j] == 1 and pos_diag[i - j + n - 1] == 1 and nag_diag[i + j] == 1:

            row[i] = j
            col[j] = 0
            pos_diag[i - j + n - 1] = 0
            nag_diag[i + j] = 0
            if i < (n - 1):
                do_queen(i + 1,n)
            else:
                output()
            col[j] = 1
            pos_diag[i - j + n - 1] = 1
            nag_diag[i + j] = 1


if __name__ == '__main__':
    col = []
    row = []
    pos_diag = []
    nag_diag = []
    count = 0
    n = int(input())
    for index in range(0, n):
        col.append(1)
        row.append(0)
    for index in range(0, 15):
        pos_diag.append(1)
        nag_diag.append(1)
    do_queen(0, n)

    print(count)