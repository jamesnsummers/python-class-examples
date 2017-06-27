""" This is a Point file """
class Point():
    """This is the Point class"""
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        """This is the string method"""
        return "({}, {})".format(self.x, self.y)

    def distance(self, p2=None):
        """This is the distance function"""
        if p2 is None:
            p2 = Point.ORIGIN
        dx = self.x - p2.x
        dy = self.y - p2.y
        return (dx ** 2 + dy ** 2) ** .5

Point.ORIGIN = Point()

print(Point.ORIGIN)

p1 = Point(3, 4)
p2 = Point(3, 19)

print(p1.distance())

print(p1.distance(p2))
