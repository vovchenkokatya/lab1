from figures_2d import Triangle, Rectangle, Trapeze, Parallelogram, Circle
from figures_3d import Ball, TriangularPyramid, QuadrangularPyramid, RectangularParallelepiped, Cone, TriangularPrism

FIGURE_MAPPING = {
    "Triangle": Triangle, "Rectangle": Rectangle, "Trapeze": Trapeze,
    "Parallelogram": Parallelogram, "Circle": Circle, "Ball": Ball,
    "TriangularPyramid": TriangularPyramid, "QuadrangularPyramid": QuadrangularPyramid,
    "RectangularParallelepiped": RectangularParallelepiped,
    "Cone": Cone, "TriangularPrism": TriangularPrism
}

def find_largest_figure(filename):
    figures = []
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            for line in f:
                parts = line.strip().split()
                if not parts or parts[0] not in FIGURE_MAPPING: continue
                try:
                    params = [float(x) for x in parts[1:]]
                    fig_obj = FIGURE_MAPPING[parts[0]](*params)
                    figures.append((parts[0], fig_obj))
                except: continue
    except FileNotFoundError:
        print(f"Файл {filename} не знайдено.")
        return

    if not figures:
        print(f"У файлі {filename} немає коректних фігур.")
    else:
        # Безпечний пошук максимуму
        res = max(figures, key=lambda x: x[1].volume() if x[1].volume() is not None else 0)
        print(f"Файл {filename}: Найбільша фігура {res[0]} з мірою {res[1].volume():.2f}")

if __name__ == "__main__":
    for i in range(1, 4):
        find_largest_figure(f'input0{i}.txt')

