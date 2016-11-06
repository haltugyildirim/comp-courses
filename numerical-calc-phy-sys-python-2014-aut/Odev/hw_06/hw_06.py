class student:
    def __init__(self):
        self.name = raw_input("Name: ")
        self.midterm = input("Midterm: ")
        self.final = input("Final: ")

    def semgrade(self):
        self.semgrade=(0.4)*self.midterm+(0.6)*self.final
        if self.semgrade >= 65.0: print self.name


N=input("Enter the number of students: ")

stu_input=[]
for i in range (N):
    stu_input.append(student())

print "The students who passed the course are: "
for j in range (N):
    stu_input[j].semgrade()
