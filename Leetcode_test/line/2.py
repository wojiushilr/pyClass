import re
_known1 = {
  'A': 0,
  'B': 1,
  'C': 2,
  'D': 3,
  'E': 4,
  'F': 5,
  'G': 6,
  'H': 7,
  'I': 8,
  }
_known2 = {
  '0': "A",
  '1': "B",
  '2': "C",
  '3': "D",
  '4': "E",
  '5': "F",
  '6': "G",
  '7': "H",
  '8': "I",
  }
def spoken_word_to_number(n):

   arr = list(n)

   for i in range(len(arr)):

    print(_known1.get(arr[i]), end="")



def number_to_spoken_word(m):


    arr = list(m)

    for i in range(len(arr)):
        print(_known2.get(arr[i]), end="")


arr = input().strip().split()

if arr[0] == "decode":

 spoken_word_to_number(arr[1])

elif arr[0] == "encode":
 number_to_spoken_word(arr[1])