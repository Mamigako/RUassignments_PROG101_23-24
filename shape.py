class Shape:
    def __init__(self) -> None:
        pass

    def __str__(self) -> str:
        return "{0} with area of {1:.2f} and perimiter of {2:.2f}".format(type(self).__name__, round(self.get_area(), 2), round(self.get_perimeter(), 2))