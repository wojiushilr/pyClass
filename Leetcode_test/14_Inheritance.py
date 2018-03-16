class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)


class Student(Person):

# Class Constructor
#
#   Parameters:
#   firstName - A string denoting the Person's first name.
#   lastName - A string denoting the Person's last name.
#   id - An integer denoting the Person's ID number.
#   scores - An array of integers denoting the Person's test scores.
#
# Write your constructor here
    def __init__(self,firstName,lastName,idNumber,score):
        super(Student,self).__init__(firstName,lastName,idNumber)
        self.score = score
#   Function Name: calculate
#   Return: A character denoting the grade.
#
# Write your function here
    def calculate(self):
        s = 0
        #print(self.score)
        for i in self.score:
            s = s+i
        avg = s//len(self.score)
        return 'O' if avg > 89 \
            else 'E' if avg > 79 \
            else 'A' if avg > 69 \
            else 'P' if avg > 54 \
            else 'D' if avg > 39 \
            else 'T'


line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input())  # not needed for Python
scores = list(map(int, input().split()))
s = Student(firstName, lastName, idNum, scores)
#s = Student("H", "B", "1", [80,100])
s.printPerson()
print("Grade:", s.calculate())