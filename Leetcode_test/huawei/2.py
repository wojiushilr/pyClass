import re
#JKLMNOPQRSTUVWXYZ
#QWERTYUIOPASDFGHJKLZXCVBNM
_known1 = {
  'A': "Q",
  'B': "W",
  'C': "E",
  'D': "R",
  'E': "T",
  'F': "Y",
  'G': "U",
  'H': "I",
  'I': "O",
  'J': "P",
  'K': "A",
  'L': "S",
    'M': "D",
    'N': "F",
    'O': "G",
    'P': "H",
    'Q': "J",
    'R': "K",
    'S': "L",
    'T': "Z",
    'U': "X",
    'V': "C",
    'W': "V",
    'X': "B",
    'Y': "N",
    'Z': "M",
    " ":" ",
'a': "q",
  'b': "w",
  'c': "e",
  'd': "r",
  'e': "t",
  'f': "y",
  'g': "u",
  'h': "i",
  'i': "o",
  'j': "p",
  'k': "a",
  'l': "s",
    'm': "d",
    'n': "f",
    'o': "g",
    'p': "h",
    'q': "j",
    'r': "k",
    's': "l",
    't': "z",
    'u': "x",
    'v': "c",
    'w': "v",
    'x': "b",
    'y': "n",
    'z': "m",
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
print(arr)

convert(arr)

