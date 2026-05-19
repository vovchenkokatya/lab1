from abc import ABC, abstractmethod

class Visitor(ABC):
    @abstractmethod
    def visit_humanitarian_student(self, student):
        pass

    @abstractmethod
    def visit_natural_student(self, student):
        pass

    @abstractmethod
    def visit_mixed_student(self, student):
        pass


class StudentElement(ABC):
    def __init__(self, target_credits, initial_money):
        self.target_credits = target_credits
        self.money = initial_money
        self.credits = 0
        self.is_expelled = False

    @abstractmethod
    def accept(self, visitor: Visitor):
        pass