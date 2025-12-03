#cretae a student class
class Student():
    def __init__(self, name, marks):
        self.name=name
        self.marks=marks

    def get_avg(self):
        sum=0
        for val in self.marks:
            sum+=val
        print("hi", self.name, "your score is", self.marks)

s1=Student("mini", [100, 99,98])
s1.get_avg()