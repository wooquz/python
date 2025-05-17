class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.grades = []

    # Добавление оценки, если она в диапазоне 0–10.
    def mark(self, grade):
        if 0 <= grade <= 10:
            self.grades.append(grade)
        else:
            print(f"Ошибка: оценка {grade} вне диапазона 0–10.")

    # Возвращение среднего балла или None, если оценок нет.
    def avg(self):
        if not self.grades:
            return None
        return sum(self.grades) / len(self.grades)

    # Вывод информации о студенте.
    def info(self):
        avg = self.avg()
        avg_str = f"{avg:.2f}" if avg is not None else "—"
        print(f"Студент: {self.name} (ID: {self.student_id})")
        print(f"Оценки: {self.grades}")
        print(f"Средний балл: {avg_str}")


# Пример использования:
if __name__ == "__main__":
    s = Student("Иван Иванов", "2025001")
    s.mark(8)
    s.mark(3)  
    s.mark(9.5)
    s.info()