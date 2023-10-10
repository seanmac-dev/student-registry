class Student:
    num = 0

    def __init__(self, name, age=13, grade="12th"):
        self._name = name
        self._age = age
        self._grade = grade
        self.student_number = Student.num + 1
        Student.num += 1

    @property
    def name(self):
        return self._name

    @name.setter
    def set_name(self, new_name):
        if (
            len(str(new_name)) > 3
            and new_name == new_name.title()
            and new_name.isalpha()
            and " " not in new_name
        ):
            self._name = new_name

    @property
    def age(self):
        return self._age

    @age.setter
    def set_age(self, new_age):
        if type(new_age) == int and 11 < new_age < 18:
            self._age = new_age

    @property
    def grade(self):
        return self._grade

    @grade.setter
    def set_grade(self, new_grade):
        grades = ["9th", "10th", "11th", "12th"]
        if new_grade in grades:
            self._grade = new_grade

    # come back to this..if range does not work, do below
    # if new_grade == "9th" or "10th" or "11th" or "12th"

    def __str__(self):
        return f"Student {self.student_number} name: {self.name}, age: {self.age}, grade: {self.grade}.\n"

    def advance(self, years_advanced=1):
        num_grade = int(self.grade[:-2])
        self.set_grade = f"{num_grade + years_advanced}th"
        print(f"{self.name} has advanced to the {self.grade} grade.")

    def study(self, subject):
        print(f"{self.name} is studying {subject}.")


student1 = Student("Alice", 45, "9th")
# student2 = Student("Sally", 99, "11th")
# student3 = Student("Joe", 14, "9th")

# print(student1)
# print(student1.grade)
# student1.advance()
# print(student1.grade)


# Step 1:
# Create student class
# Init w/ name, age, grade
# Set defaults age=13, grade="12th"
#
# Getters & Setters
# get/set name
# get/set age
# get/set grade
#
# __str__
# advance(years_advanced)
# study(subject)
#
# Step 2:
# Create 3 more student instances
# student1, student2, student3
# Use getters to print details

# Step 3:
# Test code
# Add tests
