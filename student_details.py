class Student:
    def __init__(self, name, age, department):
        self.name = name
        self.age = age
        self.department = department

        def get_details(self):
            return name, age, department
        


student_details1 = Student("Ahmed", 25, "Computer Science")
student_details2 = Student("Khalid", 26, "Computer Science")
student_details3 = Student("John", 27, "Computer Science")

#comparison officer
if student_details1.age > student_details2.age and student_details1.age > student_details3:
    print(student_details1.name, "is the oldest and he is", student_details1.age,"years old")

elif student_details2.age > student_details1.age and student_details2.age > student_details3.age:
    print(student_details2.name, "is the oldest and he is", student_details2.age,"years old")

elif student_details3.age > student_details1.age and student_details3.age > student_details2.age:
    print(student_details3.name, "is the oldest and he is", student_details3.age,"years old")
