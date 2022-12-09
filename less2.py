class Student:
    print("Hi")
    def __init__(self):
        self.height = ""
        self.age = ""
        self.sex = ""
        self.eye_color = ""
        self.grade = ""
    def printer(self):
        print(self.height)
        print(self.sex)
        print(self.grade)
        print(self.age)
        print(self.eye_color)
        #функція для виведення усіх параметрів

Yaroslaw = Student()
Oleksandra = Student()
Nazar = Student()
Sofia = Student()
#включення проекту в клас Student

Yaroslaw.height = 159
Oleksandra.height = 157
Nazar.height = 160
Sofia.height = 155

Yaroslaw.age = 13
Oleksandra.age = 12
Nazar.age = 13
Sofia.age = 13

Yaroslaw.sex = "male"
#Student.__init__(self = Yaroslaw)
#виклик інніта
Oleksandra.sex = "female"
Nazar.sex = "male"
Sofia.sex = "female"

Yaroslaw.eye_color = "green"
Oleksandra.eye_color = "gray"
Nazar.eye_color = "blue"
Sofia.eye_color = "brown"

Yaroslaw.grade = 8
Oleksandra.grade = 7
Nazar.grade = 8
Sofia.grade = 8
#задання параметрів

Oleksandra.printer()
Nazar.printer()
Sofia.printer()
Yaroslaw.printer()
#виклик функції для виведення усіх параметрів printer