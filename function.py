# class Species:
#     def _init_(self,name,diet,typical_lifespan):
#         self.name=name
#         self.diet=diet
#         self.typical_lifespan=typical_lifespan
#     def calculate_mortality_age(self,birth_year):
#         death_age=birth_year+ self.typical_lifespan
#         return death_age
#     def get_diet(self):
#         return f'{self.name} is a {self.diet}'
#     def predict_migration(self,season):
#         if season=="dry":
#             return "Migration will occur"
#         elif season=="wet":
#             return "No migration will occur"
#         else:
#             return "Unable to predict migration"
# class Predator(Species):
#     def _init_(self, name, diet, typical_lifespan, migration_patterns):
#         super()._init_(name, diet, typical_lifespan, migration_patterns)
#     def calculate_mortality_age(self,birth_year):
#         super().calculate_mortality_age()
#     def get_diet(self):
#         super().get_diet()
#     def predict_migration(self,season):
#         super().predict_migration()
# class Prey(Species):
#     def _init_(self,name, diet, typical_lifespan, migration_patterns):
#         super()._init_(name,diet, typical_lifespan, migration_patterns)
#     def calculate_mortality_age(self,birth_year):
#         super().calculate_mortality_age()
#     def get_diet(self):
#         super().get_diet()
#     def predict_migration(self,season):
#         super().predict_migration() (edited) 

# lion = Predator("Lion", "carnivore", 15, "dry season")
# gazelle = Prey("Gazelle", "herbivore", 10, "wet season")
# bear = Predator("Bear", "omnivore", 25, "none")
# fish = Prey("Fish", "carnivore", 5, "none")   
class Species:
    def __init__(self, name, diet, lifespan, migration):
        self.name = name
        self.diet = diet
        self.lifespan = lifespan
        self.migration=migration
    def display_information(self):
        print(f"{self.name} is a {self.diet} with a lifespan of {self.lifespan} years.")   
class Predator(Species):
    def __init__(self, name, diet, lifespan,migration, hunting_style):
        super().__init__(name, diet, lifespan, migration)
        self.hunting_style = hunting_style

    def display_info(self):
        super().display_information()
        print(f"hunting_style:{self.hunting_style}")     
class Prey(Species):
    def __init__(self, name, diet, lifespan, migration, speed):
        super().__init__(name, diet, lifespan, migration)
        self.speed=speed

    def display_info(self):
        super().display_information()
        print(f"speed:{self.speed}")    
lion = Predator("Lion", "Carnivore", 10, "Savannah", "Ambush")
print(lion.display_info())
gazelle = Prey("Gazelle", "Herbivore", 8, "Grasslands", 60) 
print(gazelle.display_info())     