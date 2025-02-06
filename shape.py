class Shape:
    def __init__(self, size):
        self.size = size  # Each shape has a size (like radius or area)

    # Equality comparison (==)
    def __eq__(self, other):
        return self.size == other.size

    # Less than or equal to  
    def __le__(self, other):
        return self.size <= other.size

    # Greater than or equal to  
    def __ge__(self, other):
        return self.size >= other.size

    # Less than  
    def __lt__(self, other):
        return self.size < other.size

    # Greater than  
    def __gt__(self, other):
        return self.size > other.size

    # Not equal  
    def __ne__(self, other):
        return self.size != other.size


# Example  :
shape1 = Shape(10)   
shape2 = Shape(20)   

# Testing 
print(shape1 == shape2)  # False 
print(shape1 <= shape2)  # True 
print(shape1 >= shape2)  # False 
print(shape1 < shape2)   # True 
print(shape1 > shape2)   # False 
print(shape1 != shape2)  # True (10 is not equal to 20)
