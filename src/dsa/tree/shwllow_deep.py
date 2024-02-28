class Record:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return f"({self.x}, {self.y})"

    def __repr__(self) -> str:
        return f"({self.x}, {self.y})"

p= Record(1,2)
q = Record(3,4)
l = [p, q]
t = l
temp = l.copy()
temp[0].x = 10
temp[0].y = 20

print(l)
print(t)
print(temp)