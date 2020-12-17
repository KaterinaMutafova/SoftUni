class Circle:
    __pi = 3.14

    def __init__(self, diameter):
        self.diameter = diameter
        self.radius = self.diameter / 2

    def calculate_circumference(self):
        circumference = Circle.__pi * self.diameter
        return circumference

    def calculate_area(self):
        area = Circle.__pi * pow(self.radius, 2)
        return area

    def calculate_area_of_sector(self, angle):
        sector_as_part_of_circle = 360 / angle
        area_of_sector = (angle / 360) * Circle.__pi * self.radius * self.radius
        return area_of_sector


circle = Circle(10)
angle = 5
print(f"{circle.calculate_circumference():.2f}")
print(f"{circle.calculate_area():.2f}")
print(f"{circle.calculate_area_of_sector(angle):.2f}")