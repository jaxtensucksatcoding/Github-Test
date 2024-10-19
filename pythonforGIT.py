class House:
    def __init__(self, Furniture, Model, Price):
        self.__furniture = Furniture
        self.__Model = Model
        self.__Price = Price

    def get_house_info(self):
        return f"Your house is {self.__Model}, has {self.__furniture} that cost {self.__Price}"

class type(House):
    def __init__(self, Furniture, Model, Price, extra):
        super().__init__(Furniture, Model, Price)
        self.__extra = extra

    def set_extra(self, extra):
        self.__extra = extra

    def get_extra(self):
        return f"There's a {self.__extra} too!!"

h1 = type("Sofa", "condo", "Too pricy", "Swimming pool")
print(h1.get_house_info())
print(h1.get_extra())

