
class Student:
    # Конструктор
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.grades = []

    # Добавление оценки
    def add_grade(self, grade):
        if 0 <= grade <= 10:
            self.grades.append(grade)
        else:
            print(f"Ошибка: оценка {grade} вне диапазона 0–10.")

    # Средний балл
    def get_average(self):
        return sum(self.grades) / len(self.grades) if self.grades else None

    # Вывод информации
    def display_info(self):
        avg = self.get_average()
        avg_str = f"{avg:.2f}" if avg is not None else "—"
        print(f"{self.name} (ID: {self.student_id}) — ср. балл: {avg_str}")

    # Человекочитаемое строковое представление
    def __str__(self):
        return f"Student(name={self.name}, id={self.student_id})"

    # Сравнение по student_id
    def __eq__(self, other):
        if not isinstance(other, Student):
            return False
        return self.student_id == other.student_id

    # Длина объекта = количество оценок
    def __len__(self):
        return len(self.grades)


# Пример:
if __name__ == "__main__":
    s1 = Student("Ольга", "Z123")
    s2 = Student("Ольга", "Z123")
    s3 = Student("Пётр", "P456")

    s1.add_grade(9); s1.add_grade(8)
    s2.add_grade(7)

    print(str(s1))                   # вызов __str__
    print("s1 == s2?", s1 == s2)     # True по __eq__
    print("s1 == s3?", s1 == s3)     # False
    print("Количество оценок:", len(s1))  # вызов __len__
    s1.display_info()                # вывод данных