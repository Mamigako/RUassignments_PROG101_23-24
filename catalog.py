"""Catalog class which catalogs objects of the Item class"""

class Catalog():

    def __init__(self, name) -> None:
        self.name= name
        self.list= []

    def add(self, item):
        self.list.append(item)
    
    def remove(self, item):
        if item in self.list:
            self.list.remove(item)

    def clear(self):
        self.list.clear()

    def set_name(self, name):
        self.name= name
    
    def __str__(self) -> str:
        output= f"Catalog {self.name}:\n"
        for item in self.list:
            output+= f"\t{item}\n"

        return output.rstrip("\n")
