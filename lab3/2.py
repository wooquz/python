# Базовый класс: имя и возраст
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id


class Teacher(Person):
    def __init__(self, name, subject, age):
        super().__init__(name, age)
        self.subject = subject
        self.students = []


    # Добавляет объект Student в список
    def add_student(self, student):
        if isinstance(student, Student):
            if student not in self.students:
                self.students.append(student)
                print(f"Студент {student.name} успешно добавлен.")
            else:
                print(f"Студент {student.name} уже в списке.")
        else:
            print("Можно добавить только объект класса Student.")


    # Удаляет студента по объекту или по student_id
    def remove_student(self, student):
        if student in self.students:
            self.students.remove(student)
            print(f"Студент {student.name} успешно удалён.")
        else:
            print("Студент не найден.")


    # Выводит всех студентов с их средней оценкой
    def list_students(self):
        if not self.students:
            print(f"У преподавателя {self.name} пока нет студентов.")
        else:
            print(f"Студенты преподавателя {self.name}:")
            for student in self.students:
                print(f"- {student.name} (ID: {student.student_id})")



if __name__ == "__main__":

    math_teacher = Teacher("Сквирский Михаил", "Прога python", 42)


    student1 = Student("Дробин Роман", "109428")
    student2 = Student("Максим Косов", "124532")


    math_teacher.add_student(student1)
    math_teacher.add_student(student2)
    math_teacher.add_student(student1)


    math_teacher.list_students()


    math_teacher.remove_student(student1)
    math_teacher.remove_student(Student("Несуществующий", "124980"))  


    math_teacher.list_students()