class Figure:
    unit = 'cm'
    def __init__(self):
        pass

    def calculate_area(self):
        raise "Метод должен выполнится в подклассе"
    def info(self):
        raise "Метод должен выполнится в подклассе"
    
class Square(Figure):
    def __init__(self, side_length):
        super(Square, self).__init__()
        self.side_length = side_length
    def calculate_area(self):
        side_length = self.side_length * self.side_length
        return side_length
    def info(self):
        print(f'Длина одной стороны квадрата: {str(self.side_length) + self.unit}'
                f', площадь: {str(self.calculate_area()) + self.unit}')

class Rectangle(Figure):
    def __init__(self, length, width):
        super(Rectangle, self).__init__()
        self.__length = length
        self.__width = width

    def calculate_area(self):
        area = self.__length * self.__width
        return area
    def info(self):
        print(f'Прямоугольник, длина: {str(self.__length) + self.unit}, ширина: {str(self.__width)+ self.unit}, '
              f'площадь: {str(self.calculate_area()) + self.unit}')

square1 = Square(3)
square2 = Square(5)
rectangle1 = Rectangle(6, 7)
rectangle2 = Rectangle(15, 2)
rectangle3 = Rectangle(9, 12)
list_figure = [square1,square2,rectangle1,rectangle2,rectangle3]

for figure in list_figure:
    figure.calculate_area()
    figure.info()
