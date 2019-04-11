import re
#JKLMNOPQRSTUVWXYZ
#QWERTYUIOPASDFGHJKLZXCVBNM
_known1 = {
    'A': "a",
    'B': "b",
    'C': "c",
    'D': "d",
    'E': "e",
    'F': "f",
    'G': "g",
    'H': "h",
    'I': "i",
    'J': "j",
    'K': "k",
    'L': "l",
    'M': "m",
    'N': "n",
    'O': "o",
    'P': "p",
    'Q': "q",
    'R': "r",
    'S': "s",
    'T': "t",
    'U': "u",
    'V': "v",
    'W': "w",
    'X': "x",
    'Y': "y",
    'Z': "z",
    " ":" ",
    'a': "A",
    'b': "B",
    'c': "C",
    'd': "D",
    'e': "E",
    'f': "F",
    'g': "G",
    'h': "H",
    'i': "I",
    'j': "J",
    'k': "K",
    'l': "L",
    'm': "M",
    'n': "N",
    'o': "O",
    'p': "P",
    'q': "Q",
    'r': "R",
    's': "S",
    't': "T",
    'u': "U",
    'v': "V",
    'w': "W",
    'x': "X",
    'y': "Y",
    'z': "Z",
    " ":" ",
  }

def convert(n):

   arr = n
   for i in range(len(arr)):



       if arr[i] in _known1 and   2>len(arr[i])>=0:

           print(_known1.get(arr[i]), end=" ")

       elif  len(arr[i])>=2:

           arr2 = list(arr[i])
           for j in range(len(arr2)):

               if arr2[j] in _known1:
                   print(_known1.get(arr2[j]), end="")

               else:
                   print(arr2[j], end="")


           print(" ", end="")


arr = input().strip().split()
#print(arr)

convert(arr)

