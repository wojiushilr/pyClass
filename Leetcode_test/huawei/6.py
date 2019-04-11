def search(w,g):

    eng = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q"
           ,"r","s","t","u","v","w","x","y","z"]
    for i in range(len(w)):
        v = []
        v = w[i].split()
        print(v)
        #print(len(v))
        #print(g)
        if g == v[0]:
            s = v[-2].lower()
            for i in s:
                if i in eng:
                    print(i,end="")
                else:
                    print("",format(i),end="")

    if g not in str(w):
        print("none")


if __name__ == '__main__':

    w = input().strip().split(";")
    #print("W:::::",w[0])
    #print(type(w[0]))
    v = w[0].split()
    #print("V::::::",v)
    g = input()
    search(w,g)


