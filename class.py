class Students:
    def __init__(self, name, course, gender, age):
        self.name =name
        self.cousrse = course
        self. gender = gender
        self.age = age

    def wanafunzi(self):
        print("Name: %s \nCourse: %s \n Gender: %s \n Age: %d"
              % (self.name, self.cousrse, self.gender, self.age))


stud1 = Students("Kennedy Kimani", "Computer Science", "male", 25)
stud1.wanafunzi()
stud2 = Students("Ann Mungai", "Computer Science", "Female", 30)
stud2.wanafunzi()
stud3 = Students ("Ian Mwendwa", "Django", "Male", 28)
stud3.wanafunzi()
stud4 = Students( "Mary Wambui", "Java Script ", "female", 24)
stud4. wanafunzi()
