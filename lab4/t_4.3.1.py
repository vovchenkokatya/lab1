import turtle
import math

class Figure:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    def draw(self, t):
        t.penup()
        t.goto(self.x, self.y)
        t.color(self.color)
        t.pendown()

    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y


class Circle(Figure):
    def __init__(self, x, y, radius, color):
        super().__init__(x, y, color)
        self.radius = radius

    def draw(self, t):
        super().draw(t)
        t.setheading(0)
        t.begin_fill()
        t.circle(self.radius)
        t.end_fill()


class Triangle(Figure):
    def __init__(self, x, y, side, color, angle=0):
        super().__init__(x, y, color)
        self.side = side
        self.angle = angle

    def draw(self, t):
        super().draw(t)
        t.setheading(self.angle)
        t.begin_fill()
        for _ in range(3):
            t.forward(self.side)
            t.left(120)
        t.end_fill()


class Stem(Figure):
    def __init__(self, start_x, start_y, angle, length, color="green"):
        super().__init__(start_x, start_y, color)
        self.angle = angle
        self.length = length
        self._update_endpoint()

    def _update_endpoint(self):
        rad = math.radians(self.angle)
        self.end_x = self.x + self.length * math.cos(rad)
        self.end_y = self.y + self.length * math.sin(rad)

    def draw(self, t):
        t.penup()
        t.goto(self.x, self.y)
        t.color(self.color)
        t.pensize(3)
        t.pendown()
        t.goto(self.end_x, self.end_y)
        t.pensize(1)

class Flower:
    def __init__(self, color):
        self.color = color
        self.stem = None
        self.head_center = None
        self.petals = []
        self.leaves = []

    def setup_geometry(self, base_x, base_y, angle, length):
        # 1. Стебло
        self.stem = Stem(base_x, base_y, angle, length)
        hx, hy = self.stem.end_x, self.stem.end_y

        self.head_center = Circle(hx, hy, 8, "yellow")
        p_rad = 10
        self.petals = [
            Circle(hx + 12, hy + 2, p_rad, self.color),
            Circle(hx - 12, hy + 2, p_rad, self.color),
            Circle(hx, hy + 14, p_rad, self.color),
            Circle(hx, hy - 10, p_rad, self.color)
        ]

        mid_x = base_x + (length * 0.4) * math.cos(math.radians(angle))
        mid_y = base_y + (length * 0.4) * math.sin(math.radians(angle))
        self.leaves = [
            Triangle(mid_x, mid_y, 20, "forest green", angle + 45),
            Triangle(mid_x, mid_y, 20, "forest green", angle - 135)
        ]

    def draw(self, t):
        self.stem.draw(t)
        for leaf in self.leaves:
            leaf.draw(t)
        for p in self.petals:
            p.draw(t)
        self.head_center.draw(t)


class Bouquet:
    def __init__(self):
        self.base_x = 0
        self.base_y = -250
        self.flowers = []
        colors = ["red", "orange", "magenta", "purple", "pink", "deep pink", "dark red"]

        for i in range(7):
            angle = 70 + (i * 7)  # Кути для віяла
            length = 300 - (abs(i - 3) * 25)
            f = Flower(colors[i])
            f.setup_geometry(self.base_x, self.base_y, angle, length)
            self.flowers.append(f)

    def draw(self, t):
        for f in self.flowers:
            f.draw(t)

    def move(self, dx, dy):
        self.base_x += dx
        self.base_y += dy
        for f in self.flowers:
            f.setup_geometry(self.base_x, self.base_y, f.stem.angle, f.stem.length)

def render():
    painter.clear()
    my_bouquet.draw(painter)
    screen.update()


if __name__ == "__main__":
    screen = turtle.Screen()
    screen.setup(800, 800)
    screen.tracer(0)

    painter = turtle.Turtle()
    painter.hideturtle()

    my_bouquet = Bouquet()
    render()
    def move_action():
        my_bouquet.move(-40, 20)
        render()


    screen.onkey(move_action, "space")
    screen.listen()

    print("Натисніть SPACE, щоб перемістити букет!")
    screen.mainloop()