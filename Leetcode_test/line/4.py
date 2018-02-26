def main(argv):
    # このコードは引数と標準出力を用いたサンプルコードです。
    # このコードは好きなように編集・削除してもらって構いません。
    # ---
    # This is a sample code to use arguments and outputs.
    # Edit and remove this code as you like.

        l = len(argv)

        for i in range(l):

            str_temp = list(argv[i])
            #print(type(int(argv[i])))
            #print(str_temp)
            #print(i)
            if argv[i].isdigit() == False:
                print("invalid")
            else:
                num1 = 0
                for j in str_temp:
                    if j == "3":
                      num1 = num1 + 1


                if num1 > 0 and int(argv[i]) % 3==0:
                        print("dumb")
                elif num1 > 0:
                        print("stupid")
                elif int(argv[i]) % 3 == 0:
                    print("idiot")
                else :
                    print("smart")






arr = ["90"]
main(arr)