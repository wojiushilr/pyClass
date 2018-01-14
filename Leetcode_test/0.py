import sys


def solve(a0, a1, a2, b0, b1, b2):
    # Complete this function
    ascore = 0
    bscore = 0
    if a0 > b0:
        ascore = ascore + 1
    else:
        bscore = bscore + 1

    if a1 > b1:
        ascore = ascore + 1
    else:
        bscore = bscore + 1

    if a2 > b2:
        ascore = ascore + 1
    else:
        bscore = bscore + 1

    result = [ascore, bscore]
    return result


a0, a1, a2 = input().strip().split(' ')
a0, a1, a2 = [int(a0), int(a1), int(a2)]
b0, b1, b2 = input().strip().split(' ')
b0, b1, b2 = [int(b0), int(b1), int(b2)]
result = solve(a0, a1, a2, b0, b1, b2)
print(" ".join(map(str, result)))