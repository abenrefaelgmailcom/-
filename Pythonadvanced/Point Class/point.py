
class Point:
    """
    Represents a point in a 2D coordinate system.
    """

    # Initialize the point with x and y coordinates.
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Move the point to the left.
    def move_left(self, value):
        self.x -= value

    # Move the point to the right.
    def move_right(self, value):
        self.x += value

    # Move the point upward.
    def move_up(self, value):
        self.y += value

    # Move the point downward.
    def move_down(self, value):
        self.y -= value

    # Return a readable string representation.
    def __str__(self):
        return f"Point(x={self.x}, y={self.y})"


# Example usage - DO NOT CHANGE

p1 = Point(x=5.4, y=8.1)
print(p1)

p1.move_right(2.5)
p1.move_up(3)

print(p1)