class Zoo:
    __animals = 0 # attribute e private zaradi __ tozi koito ne moje da se dostupe izvun classa i moje da se dostupe v clasaa # class atribute

    def __init__(self, name):
        self.name = name # instance atribute
        self.mammals =[]
        self.fishes = []
        self.birds = []
    def add_animal(self, species , name):
        self.__animals += 1
        if species == "mammal":
            self.mammals.append(name)
        elif species == "fish":
            self.fishes.append(name)
        elif species == "bird":
            self.birds.append(name)

        #Zoo.__animals += 1

    def get_info(self, species):
        result = ""
        if species == "mammal":
            result += f"Mammals in {self.name}: {', '.join(self.mammals)}\n"

        elif species == "fish":
            result += f"Fishes in {self.name}: {', '.join(self.fishes)}\n"

        elif species == "bird":
            result += f"Birds in {self.name}: {', '.join(self.birds)}\n"

        result += f"Total anuimals: {Zoo.__animals}"
        return result


zoo_name = input()
zoo = Zoo(zoo_name)
count = int(input())

for i in range(count):
    animal = input().split(" ")
    species = animal[0]
    name = animal[1]
    zoo.add_animal(species, name)

info = input()
print(zoo.get_info(info))


# class Zoo:
#     __animals = 0
#
#     def __init__(self, name):
#         self.name = name
#         self.mammals = []
#         self.fishes = []
#         self.birds = []
#
#     def add_animal(self, species, name):
#         # self.__animals += 1
#         Zoo.__animals += 1
#
#         if species == "mammal":
#             self.mammals.append(name)
#         elif species == "fish":
#             self.fishes.append(name)
#         elif species == "bird":
#             self.birds.append(name)
#
#     def get_info(self, species):
#         animals_names = None
#         res = ""
#         if species == "mammal":
#             animals_names = self.mammals
#             res = "Mammals"
#         elif species == "fish":
#             animals_names = self.fishes
#             res = "Fishes"
#         elif species == "bird":
#             animals_names = self.birds
#             res = "Birds"
#
#         animals_data = ", ".join(animals_names)
#         return f"""{res} in {self.name}: {animals_data}
# Total animals: {Zoo.__animals}"""
#
#
# zoo_name = input()
# n = int(input())
# zoo = Zoo(zoo_name)
#
# for i in range(n):
#     args = input().split()
#     zoo.add_animal(args[0], args[1])
#
# species_type = input()
# res = zoo.get_info(species_type)
# print(res)