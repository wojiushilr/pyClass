'''
这是line的数字转换题
'''

def unit_to_word(u):
    convert_table = {
        0:"zero",
        1:"one",
        2:"two",
        3:"three",
        4:"four",
        5:"five",
        6:"six",
        7:"seven",
        8:"eight",
        9:"nine",
        ".":"point",
    }
    return convert_table[u]
def tens_to_word(t):

    convert_table = {
        0: "",
        10: "ten",
        11: "eleven",
        12: "twelve",
        13: "thirteen",
        14: "fourteen",
        15: "fifteen",
        16: "sixteen",
        17: "seventeen",
        18: "eighteen",
        19: "nineteen",
        2: "twenty",
        3: "thirty",
        4: "forty",
        5: "fifty",
        6: "sixty",
        7: "seventy",
        8: "eighty",
        9: "ninety",
    }
    if 9 < t < 20:
        return convert_table[t]
    else:
        tens = convert_table[t//10] + "" + unit_to_word(t%10)
        return tens

def main(h):

    h = int(h[0])
    if h > 99:
        word = unit_to_word(h//100) + " hundred"
        tens = h % 100
        if tens == 0:
            #print(type(word))
            print(word.upper().capitalize())
        else:
            print(word.upper().capitalize() + " and " + tens_to_word(tens))

    else:

        #print(type(tens_to_word(h)))
        print(tens_to_word(h).upper().capitalize())



arr = ["100"]
arr2 = ["8"]
main(arr2)
print("One hundred")