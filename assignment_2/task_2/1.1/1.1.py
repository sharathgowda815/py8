class parent:

    print('Enter the lengths of sides of triangle')
    a = int(input('Side A = '))
    b = int(input('Side B = '))
    c = int(input('Side C = '))

class area_of_triangle(parent):

    def areaoftriangle(self):
        s = (self.a + self.b + self.c) / 2
        return str((s*(s-self.a)*(s-self.b)*(s-self.c)) ** 0.5)

print('Area of triangle is ' + area_of_triangle.areaoftriangle(self=parent))