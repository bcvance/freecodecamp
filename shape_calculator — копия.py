class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def __repr__(self):
        return f"Rectangle(width={self.width}, height={self.height})"
    def set_width(self, new_width):
        self.width = new_width
    def set_height(self, new_height):
        self.height = new_height
    def get_area(self):
        return self.width * self.height
    def get_perimeter(self):
        return 2*self.width + 2*self.height
    def get_diagonal(self):
        return (self.width**2 + self.height**2)**0.5
    # this method creates an image of the square or rectangle using asterisks
    def get_picture(self):
        output_string = ""
        if self.width > 50 or self.height > 50:
          return "Too big for picture."
        else:
          for i in range(self.height):
              output_string += "*"*self.width + "\n"
          return output_string
    # this method determines how many of one square or rectangle can fit inside another
    def get_amount_inside(self, shape):
        horizontal_fit = self.width/shape.width
        vertical_fit = self.height/shape.height
        total_inside = int(horizontal_fit*vertical_fit)
        return total_inside

class Square(Rectangle):
    def __init__(self, side):
        self.width = side
        self.height = side
    def __repr__(self):
        return f"Square(side={self.width})"
    def set_width(self, new_width):
        self.width = new_width
        self.height = new_width
    def set_height(self, new_height):
        self.height = new_height
        self.width = new_height
    def set_side(self, new_side):
        self.width = new_side
        self.height = new_side
