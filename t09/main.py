import os
from students import HumanitarianStudent, NaturalStudent, MixedStudent
from visitors import (
    TeachHumanitarian, TeachNatural,
    PayHostel, PayFood,
    ObtainScholarship, ObtainMoney
)

def simulate_student_life(file_path):
    # Перевіряємо чи існує файл
    if not os.path.exists(file_path):
        print(f"Помилка: Файл {file_path} не знайдено.")
        return

    with open(file_path, "r", encoding="utf-8") as file:
        lines = file.readlines()

    if not lines:
        return

    student_type = lines[0].strip().lower()
    target_credits = int(lines[1].strip())
    initial_money = int(lines[2].strip())

    if "humanitarian" in student_type:
        student = HumanitarianStudent(target_credits, initial_money)
    elif "natural" in student_type and "mixed" not in student_type:
        student = NaturalStudent(target_credits, initial_money)
    else:
        student = MixedStudent(target_credits, initial_money)

    for line in lines[3:]:
        line = line.strip()
        if not line or student.is_expelled:
            continue

        parts = line.split()
        action = parts[0].lower()
        visitor = None

        if action == "teach":
            subject, val = parts[1].lower(), int(parts[2])
            if subject == "humanitarian":
                visitor = TeachHumanitarian(val)
            elif subject == "natural":
                visitor = TeachNatural(val)

        elif action == "pay":
            target, val = parts[1].lower(), int(parts[2])
            if target == "hostel":
                visitor = PayHostel(val)
            elif target == "food":
                visitor = PayFood(val)

        elif action == "obtain":
            source, val = parts[1].lower(), int(parts[2])
            if source == "scholarship":
                visitor = ObtainScholarship(val)
            elif source == "money":
                visitor = ObtainMoney(val)

        if visitor:
            student.accept(visitor)

    print(f"Тип студента: {student.__class__.__name__}")
    print(f"Баланс: {student.money} грн, Кредити: {student.credits}/{student.target_credits}")

    if student.is_expelled:
        print("Вердикт: Відраховано за несплату. Диплом НЕ отримано.\n")
    elif student.credits >= student.target_credits:
        print("Вердикт: Успіх! Диплом отримано.\n")
    else:
        print("Вердикт: Не вистачило кредитів для диплому.\n")

if __name__ == "__main__":

    test_file = "input01.txt"
    simulate_student_life(test_file)