import math
class Shape:
	def __init__(self, name):
		self.name = name

	def get_name(self):
		return self.name

class Circle:
	def __init__(self, name, radius):
		 self.name = name
		 self.radius = radius

	def calc_area(self):
		return  self.radius* self.radius*math.pi

	def calc_perimeter(self):
		return  self.radius*2*math.pi

class Rectangle:
	def __init__(self, name, width, height):
		self.name = name
		self.width = width
		self.height = height

	def calc_area(self):
		return self.width*self.height

	def calc_perimeter(self):
		return 2*(self.width+self.height)

def main():
	circle1 = Circle("fancy", 5)
	print(circle1.calc_area())
	print(circle1.calc_perimeter())

	rectangle1 = Rectangle("lucky", 3, 4)
	print(rectangle1.calc_area())
	print(rectangle1.calc_perimeter())

if __name__ == '__main__':
    main()
	
