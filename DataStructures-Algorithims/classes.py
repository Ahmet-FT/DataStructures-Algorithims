class Student:

    count = 0
    total_gpa = 0

    def __init__(self, name, gpa = 0):
        self.name = name
        self.gpa = gpa
        Student.count += 1
        Student.total_gpa += gpa


    def get_info(self):
        return f"{self.name} {self.gpa}"
    
    @classmethod
    def get_count(cls):
        return f"Number of students: {cls.count}"
    @classmethod
    def get_avarage_gpa(cls):
        return f"Average GPA: {(cls.total_gpa/cls.count):.2f}"
    

#student1 = Student("Spongebob", 3.5)
#student2 = Student("Patrick", 2.0)
#student3 = Student("Sandy", 4.0)

students = [Student("Spongebob", 3.5), Student("Patrick", 2.0), Student("Sandy", 4.0)]
#student1.gpa = 3.5
for i in students:
    print(i.get_info())

print(Student.get_count())

print(Student.get_avarage_gpa())