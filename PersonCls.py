class Point:
    def __int__(self, x, y):
        self.x=x
        self.y=y

    def move(self):
        print("Move the point")

    def draw(self):
        print("draw the point")


point1 = Point()
point1.move()

