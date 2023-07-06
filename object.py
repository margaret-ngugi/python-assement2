#**African Cuisine:** You're creating a recipe app specifically for African cuisine.
#The app needs to handle recipes from different African countries, each with its
#unique ingredients, preparation time, cooking method, and nutritional
#information. Consider creating a `Recipe` class, and think about how you might
#create subclasses for different types of recipes (e.g., `MoroccanRecipe`,
#EthiopianRecipe`, `NigerianRecipe`), each with their own unique properties and
#Methods.


# class Recipe:
    
#     def __init__( name ,ingredients, preparation_time, cooking_method, nutritional_information):
        
       
#         self.ingredients = ingredients
#         self.preparation_time = preparation_time
#         self.cooking_method = cooking_method
#         self.nutritional_information = nutritional_information

#     def __str__(self):
        
#         return f"{self.name} ({self.preparation_time} minutes)"

#     def display_recipe_properties(self):
        
#         print(f"Name: {self.name}")
#         print(f"Ingredients: {self.ingredients}")
#         print(f"Preparation time: {self.preparation_time}")
#         print(f"Cooking method: {self.cooking_method}")
#         print(f"Nutritional information: {self.nutritional_information}")

# class MoroccanRecipe(Recipe):
   

#     def __init__(self, name, ingredients, preparation_time, cooking_method, nutritional_information, tagine_type, spices):
       
#         super().__init__(name, ingredients, preparation_time, cooking_method, nutritional_information)
#         self.tagine_type = tagine_type
#         self.spices = spices

#     def __str__(self):
       
#         return f"{self.name} ({self.preparation_time} minutes) - {self.tagine_type} tagine with {self.spices}"

#     def suggest_combinations(self):
        
#         print(f"This recipe can be paired with couscous, salad, or bread.")

#     def get_nature_of_dish(self):
#         """Return the nature of the dish (spicy or not)."""
#         if "chili" in self.ingredients:
#             return "spicy"
#         else:
#             return "not spicy"    
# recipe1 = Recipe("Pasta Carbonara", ["spaghetti", "bacon", "eggs", "parmesan cheese"], 30, "boiling", "High in calories")
# recipe1.display_recipe_properties()


# moroccan_recipe1 = MoroccanRecipe("Chicken Tagine", ["chicken", "onion", "olives", "lemon", "spices"], 60, "slow cooking", "Rich in flavors", "Traditional", ["cumin", "coriander", "paprika"])
# print(moroccan_recipe1)
# moroccan_recipe1.suggest_combinations()
# print(moroccan_recipe1.get_nature_of_dish())


#Q3
#You're a wildlife conservationist working on a
#program to track different species in a national park. Each species has its own
#characteristics and behaviors, such as its diet, typical lifespan, migration
#patterns, etc. Some species might be predators, others prey. You'll need to
#create classes to model `Species`, `Predator`, `Prey`, etc., and think about how
#these classes might relate to each other through inheritance

class Species:
    def __init__(self, name, diet, lifespan, migration_patterns):
        self.name = name
        self.diet = diet
        self.lifespan = lifespan
        self.migration_patterns = migration_patterns

    def display_information(self):
        return f"{self.name} is a {self.diet} with a lifespan of {self.lifespan} years."


class Predator(Species):
    def __init__(self, name, diet, lifespan, migration_patterns, prey):
        super().__init__(name, diet, lifespan, migration_patterns)
        self.prey = prey

    def __str__(self):
        return f"{self.name} is a predator that preys on {self.prey}."


class Prey(Species):
    def __init__(self, name, diet, lifespan, migration_patterns, predators):
        super().__init__(name, diet, lifespan, migration_patterns)
        self.predators = predators

    def __str__(self):
        return f"{self.name} is a prey that is preyed upon by {self.predators}."


#Create a class called Product with attributes for name, price, and quantity.
#Implement a method to calculate the total value of the product (price * quantity).
#Create multiple objects of the Product class and calculate their total values.
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_value(self):
        return self.price * self.quantity


product1 = Product("iPhone", 1000, 1)
product2 = Product("iPad", 500, 2)

print(product1.calculate_total_value())
# 1000

print(product2.calculate_total_value())
# 1000

#6.Implement a class called Student with attributes for name, age, and grades (a
#list of integers). Include methods to calculate the average grade, display the
#student information, and determine if the student has passed (average grade >=
#60). Create objects for the Student class and demonstrate the usage of these
#methods.provide code in python


class Student:
    def __init__(self, name, age, grades):
        self.name = name
        self.age = age
        self.grades = grades

    def calculate_average_grade(self):
        total_grades = sum(self.grades)
        return total_grades / len(self.grades)

    def display_student_information(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Grades:", self.grades)

    def has_passed(self):
        if self.calculate_average_grade()>=60:
            return"the student has passed"
        else:
            return "the student has failed"    

        # return self.calculate_average_grade() >= 60


student1 = Student("John Doe", 10, [50, 50, 50])
student2 = Student("Jane Doe", 19, [80, 70, 60])

print(student1.calculate_average_grade())
print(student2.calculate_average_grade())



print(student1.has_passed())
print(student2.has_passed())


#Create a LibraryCatalog class that handles the cataloging and management of
#books in a library. Implement methods to add new books, search for books by
#title or author, keep track of available copies, and display book details.

#QUIZ8
class LibraryCatalog:

    def __init__(self):
        self.books = []

    def add_book(self, title, author, num_copies):
        book = {
            "title": title,
            "author": author,
            "num_copies": num_copies,
        }
        self.books.append(book)

    def search_by_title(self, title):
        for book in self.books:
            if book["title"] == title:
                return book
        return None

    def search_by_author(self, author):
        for book in self.books:
            if book["author"] == author:
                return book
        return None

    def get_num_available_copies(self, title):
        book = self.search_by_title(title)
        if book is None:
            return 0
        return book["num_copies"]

    def display_book_details(self, title):
        book = self.search_by_title(title)
        if book is None:
            print("Book not found")
            return
        print("Title:", book["title"])
        print("Author:", book["author"])
        print("Number of copies:", book["num_copies"])



    catalog = LibraryCatalog()
    # catalog.add_book("The Hitchhiker's Guide to the Galaxy", "Douglas Adams", 10)
    catalog.add_book("The Lord of the Rings", "J.R.R. Tolkien", 5)
    print(catalog.get_num_available_copies("The Hitchhiker's Guide to the Galaxy"))
    print(catalog.search_by_author("Douglas Adams"))
    catalog.display_book_details("The Lord of the Rings")
