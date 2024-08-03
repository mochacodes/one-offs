
#putting an underscore before the variable denotes that it is private.

class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def width(self):
        return f"{self._width}cm"

    @property
    def height(self):
        return f"{self._height}cm"

    @width.setter
    def width(self, new_width):
        if new_width > 0:
            self._width = new_width
        else:
            print("width must be greater than 0")

    @height.setter
    def height(self, new_height):
        if new_height > 0:
            self._height = new_height
        else:
            print("height must be greater than 0")

    @width.deleter
    def width(self):
        del self._width
        print("width was deleted.")

    @height.deleter
    def height(self):
        del self._height
        print("height was deleted.")

    def __str__(self):
        return f"W: {self.width} H: {self.height}"




rect = Rectangle(3, 4)
print(rect)
rect.height = 6
rect.width = 6

print(rect)
print(rect.width)
print(rect.height)

