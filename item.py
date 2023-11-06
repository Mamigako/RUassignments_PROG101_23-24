"""Item class which with name and category attributes."""

class Item():

    def __init__(self, name, category) -> None:
        self.name= name
        self.category= category

    def set_name(self, name):
        self.name= name

    def set_category(self, category):
        self.category= category

    def __str__(self) -> str:
        return f"Name: {self.name}, Category: {self.category}"
