from interfaces import Visitor

class TeachHumanitarian(Visitor):
    def __init__(self, credits_val):
        self.credits_val = credits_val

    def visit_humanitarian_student(self, student):
        student.credits += self.credits_val

    def visit_natural_student(self, student):
        pass

    def visit_mixed_student(self, student):
        student.credits += self.credits_val


class TeachNatural(Visitor):
    def __init__(self, credits_val):
        self.credits_val = credits_val

    def visit_humanitarian_student(self, student):
        pass

    def visit_natural_student(self, student):
        student.credits += self.credits_val

    def visit_mixed_student(self, student):
        student.credits += self.credits_val


class FinancialOperation(Visitor):
    def __init__(self, amount):
        self.amount = amount

    def process_finance(self, student):
        student.money += self.amount
        if student.money < 0:
            student.is_expelled = True

    def visit_humanitarian_student(self, student):
        self.process_finance(student)
    def visit_natural_student(self, student):
        self.process_finance(student)
    def visit_mixed_student(self, student):
        self.process_finance(student)


class PayHostel(FinancialOperation):
    def __init__(self, amount):
        super().__init__(-amount)


class PayFood(FinancialOperation):
    def __init__(self, amount):
        super().__init__(-amount)


class ObtainScholarship(FinancialOperation):
    def __init__(self, amount):
        super().__init__(amount)


class ObtainMoney(FinancialOperation):
    def __init__(self, amount):
        super().__init__(amount)