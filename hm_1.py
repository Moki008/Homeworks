class Person:
    def __init__(self,full_name, age, is_married):
        self.full_name = full_name
        self.age = age
        self.is_married = is_married

    def introduce_myself(self):
        print(f'Full name: {self.full_name}, age: {self.age},is_married: {self.is_married} ')

class Student(Person):
    def __init__(self, full_name, age, is_married, marks):
        super().__init__(full_name, age, is_married)
        self.marks = marks
    def calculate_marks(self):
        mid_marks = sum(self.marks.values())/len(self.marks)
        return mid_marks
    def introduce_myself(self):
        super().introduce_myself()
        print(f"Оценки: {self.marks}")
        print(f"Средняя оценка: {round(self.calculate_marks(), 1)}")

class Teacher(Person):
    base_salary = 30000

    def __init__(self, full_name, age, is_married, experience):
        super().__init__(full_name, age, is_married)
        self.experience = experience

    def calculate_salary(self):
        if self.experience > 3:
                for i in range(self.experience):
                    if self.base_salary % 3 == 0:
                        bonus = (self.experience // 3) * (self.base_salary * 0.05)
                        return self.base_salary + bonus
        return self.base_salary

    def introduce_myself(self):
        super().introduce_myself()
        print(f"Experience: {self.experience} years")
        print(f"Salary: {self.calculate_salary()}")
def create_students():
    student1 = Student("Иван Иванов", 16, False, {"Математика": 5, "Физика": 4, "Химия": 3})
    student2 = Student("Анна Петрова", 17, False, {"Черчение": 4, "Физика": 4, "Биология": 4})
    student3 = Student("Олег Смирнов", 15, False, {"История": 3, "Лит-ра": 5, "География": 3})
    students = [student1, student2, student3]
    return students
for student in create_students():
    student.introduce_myself()