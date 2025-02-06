class Shape:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def __add__(self, other):
        # Adding the dimensions of two rectangles
        x = self.length + other.length
        y = self.width + other.width
        return Shape(x, y)

    def __sub__(self, other):
        # Subtracting the dimensions of two rectangles 
        x = max(0, self.length - other.length)
        y = max(0, self.width - other.width)
        return Shape(x, y)

    def __truediv__(self, other):
        # Dividing the dimensions of two rectangles 
        if other.length == 0 or other.width == 0:
            raise ValueError("Cannot divide by a rectangle with zero length or width.")
        x = self.length / other.length
        y = self.width / other.width
        return Shape(x, y)

    def __mul__(self, other):
        if isinstance(other, Shape):
            # Multiplying two rectangles (area multiplication)
            x = self.length * other.length
            y = self.width * other.width
            return Shape(x, y)
        elif isinstance(other, (int, float)):
            # Scalar multiplication (scale the rectangle's dimensions)
            x = self.length * other
            y = self.width * other
            return Shape(x, y)
        else:
            raise ValueError("Multiplication is only supported with another Shape or a scalar.")

    def __repr__(self) -> str:
        return f'Shape({self.length}, {self.width})'

# usage:

r1 = Shape(3, 10)
r2 = Shape(2, 5)
r3 = Shape(1, 2)

print(r1 + r2)  

print(r1 - r2)  

print(r1 / r2)  

print(r1 * r2) 

print(r1 * 3)  
