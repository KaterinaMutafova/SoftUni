class Zoo:
    __animals = 0
    def __init__(self, name):
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, species, name):
        if species == "mammal":
            self.mammals.append(name)
        elif species == "fish":
            self.fishes.append(name)
        elif species == "bird":
            self.birds.append(name)
        Zoo.__animals += 1

    def get_info(self, species):
        animals_to_display = []
        result = ""
        if species == "mammal":
            animals_to_display = self.mammals
            result += f"Mammals in {zoo_name}: {', '.join(animals_to_display)} \n"
        elif species == "fish":
            animals_to_display = self.fishes
            result += f"Fishes in {zoo_name}: {', '.join(animals_to_display)} \n"
        elif species == "bird":
            animals_to_display = self.birds
            result += f"Birds in {zoo_name}: {', '.join(animals_to_display)} \n"
        result += f"Total animals: {zoo.__animals}"

        return result


zoo_name = input()
rows_n = int(input())

zoo = Zoo(zoo_name)

for i in range(rows_n):
    animals = input()
    species, name = animals.split(" ")
    zoo.add_animal(species, name)

info = input()
print(zoo.get_info(info))





