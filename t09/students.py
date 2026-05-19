from interfaces import StudentElement, Visitor

class HumanitarianStudent(StudentElement):
    def accept(self, visitor: Visitor):
        visitor.visit_humanitarian_student(self)


class NaturalStudent(StudentElement):
    def accept(self, visitor: Visitor):
        visitor.visit_natural_student(self)


class MixedStudent(StudentElement):
    def accept(self, visitor: Visitor):
        visitor.visit_mixed_student(self)