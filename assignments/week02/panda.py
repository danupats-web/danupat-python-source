class circle:
    def __init__(self):
        self.radius = float(input("Enter radius: "))

    def calculate_circle_area(self):
        return 3.14 * self.radius * self.radius

    def calculate_circle_perimeter(self):
        return 2 * 3.14 * self.radius

c = circle()
print(c.calculate_circle_area())
print(c.calculate_circle_perimeter())