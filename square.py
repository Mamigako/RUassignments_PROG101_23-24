from rectangle import Rectangle
class Square(Rectangle):
    def __init__(self, size) -> None:
        super().__init__(size, size)

    