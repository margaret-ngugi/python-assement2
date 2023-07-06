#Q1
#**Ancestral Stories:** In many African cultures, the art of storytelling is passed
#down from generation to generation. Imagine you're creating an application that
#records these oral stories and translates them into different languages. The
#stories vary by length, moral lessons, and the age group they are intended for.
#Think about how you would model `Story`, `StoryTeller`, and `Translator`
#objects, and how inheritance might come into play if there are different types of
#stories or storytellers.

class Story:
    def __init__(self, title, content, moral, age_group):
        self.title = title
        self.content = content
        self.moral = moral
        self.age_group = age_group

    def display(self):
        print(f"Title: {self.title}")
        print(f"Content: {self.content}")
        print(f"Moral: {self.moral}")
        print(f"Age Group: {self.age_group}")


class StoryTeller:
    def __init__(self, name, language):
        self.name = name
        self.language = language

    def tell_story(self, story):
        print(f"{self.name} is telling a story in {self.language}:")
        story.display()


class Translator(StoryTeller):
    def __init__(self, name, language, target_language):
        super().__init__(name, language)
        self.target_language = target_language

    def translate(self, story):
        # Translate the story into the target language
        # (Implementation details depend on your translation mechanism)
        translated_content = translate_function(story.content, self.language, self.target_language)

        translated_story = Story(story.title, translated_content, story.moral, story.age_group)
        return translated_story


# Example usage
story1 = Story("The Lion and the Mouse", "Once upon a time...", "Helping others is important.", "Children")
story2 = Story("The Tortoise and the Hare", "In a forest, there was a hare who always...", "Slow and steady wins the race.", "Children")

storyteller = StoryTeller("Kwame", "English")
storyteller.tell_story(story1)

translator = Translator("Amara", "Swahili", "French")
translated_story = translator.translate(story2)
storyteller.tell_story(translated_story)

#1. inputs,length,moral_lesson,age
#2. process ,creating a class and passing attributes in the function constructor,adding methods
#3.output,records of oral stories and translates into different languages
class OralStories:
    def __init__(self,length,moral_lesson,age_group):
        self.length=length
        self.moral_lesson=moral_lesson
        self.age_proup=age_group

    def record_story(self,story):
        if self.length<50 and self.moral_lesson=="obedient" and self.age_group<15:
            return f"this {story} is recorded for children"
        elif self.length>50 and self.moral_lesson=="hardworking" and self.age_group>15:
            return f"this {story} is recorded for students" 
        else:
            return f"this {story} is recorded for adults" 

    def translate_story(self,languages):
        if self.length<50 and self.moral_lesson=="obedient" and self.age_group<15:
            return f"this {story} is tranlated to kiswahili"
        elif self.length>50 and self.moral_lesson=="hardworking" and self.age_group>15:
            return f"this {story} is translated to English" 
        else:
            return f"this {story} istranslated to mother tongue" 

            



#Q2        
#**African Cuisine:** You're creating a recipe app specifically for African cuisine.
#The app needs to handle recipes from different African countries, each with its
#unique ingredients, preparation time, cooking method, and nutritional
#information. Consider creating a `Recipe` class, and think about how you might
#create subclasses for different types of recipes (e.g., `MoroccanRecipe`,
#EthiopianRecipe`, `NigerianRecipe`), each with their own unique properties and
#methods. 

class Recipe:
    def __init__(self, name, country, ingredients, preparation_time, cooking_method, nutritional_info):
        self.name = name
        self.country = country
        self.ingredients = ingredients
        self.preparation_time = preparation_time
        self.cooking_method = cooking_method
        self.nutritional_info = nutritional_info

class MoroccanRecipe(Recipe):
    def __init__(self, name, ingredients, preparation_time, cooking_method, nutritional_info, spice_level):
        super().__init__(name, "Morocco", ingredients, preparation_time, cooking_method, nutritional_info)
        self.spice_level = spice_level

class EthiopianRecipe(Recipe):
    def __init__(self, name, ingredients, preparation_time, cooking_method, nutritional_info, injera_required):
        super().__init__(name, "Ethiopia", ingredients, preparation_time, cooking_method, nutritional_info)
        self.injera_required = injera_required

class NigerianRecipe(Recipe):
    def __init__(self, name, ingredients, preparation_time, cooking_method, nutritional_info, jollof_rice_base):
        super().__init__(name, "Nigeria", ingredients, preparation_time, cooking_method, nutritional_info)
        self.jollof_rice_base = jollof_rice_base

# Example usage
moroccan_tagine = MoroccanRecipe("Chicken Tagine", ["chicken thighs", "onion", "garlic", "ginger", "preserved lemon", "green olives", "spices"], "1 hour", "Stovetop", "Calories: 400", "Medium")
ethiopian_tibs = EthiopianRecipe("Beef Tibs", ["beef", "onion", "tomato", "jalapeno", "spices"], "45 minutes", "Stovetop", "Calories: 450", True)
nigerian_jollof = NigerianRecipe("Jollof Rice", ["rice", "tomato", "onion", "pepper", "spices", "chicken broth", "vegetable oil"], "1 hour 30 minutes", "Stovetop", "Calories: 300", True)
class Recipe:
    def __init__(self,unique_ingredients,preparation_time,cooking_method,nutritional_information):
        self.unique_ingredients=unique_ingredients
        self.preparation_time=preparation_time
        self.cooking_method=cooking_method
        self.nutritional_information=nutritional_information
    def check_different_recipe(self,recipe):
        print(f"{self}.__class.__.__{name}.__:{self.recipe}") 

class MoroccanRecipe(Recipe):
    recipe="takes too many ingredients ,more time and have more nutritional value" 
class EthiopianRecipe(Recipe):
    recipe= "takes less ingredients ,less time and have less nutritional value" 
class NigerianRecipe(Recipe):
    recipe= "takes egual ingredients ,minimum time and have minimum nutritional value" 


    #QUESTION2
    class Recipe:
    def __init__(self, name, prep_time, cook_method, nutrition):
        self.name = name
        self.prep_time = prep_time
        self.cook_method = cook_method
        self.nutrition = nutrition
    def display_recipe(self):
        return f"The {self.name} recipe in Africa is prepared with specific ingredients. It takes about {self.prep_time} to cook using {self.cook_method}. It has high {self.nutrition}."
class AfricanRecipe(Recipe):
    def __init__(self, name, prep_time, cook_method, nutrition):
        super().__init__(name, prep_time, cook_method, nutrition)
    def prepare(self):
        return f"The {self.name} recipe in Africa is being prepared."
class EthiopianRecipe(Recipe):
    def __init__(self, name, prep_time, cook_method, nutrition):
        super().__init__(name, prep_time, cook_method, nutrition)
    def prepare(self):
        return f"The {self.name} recipe in Ethiopia is being prepared."
class NigerianRecipe(Recipe):
    def __init__(self, name, prep_time, cook_method, nutrition):
        super().__init__(name, prep_time, cook_method, nutrition)
    def prepare(self):
        return f"The {self.name} recipe in Nigeria is being prepared."
African_pizza = AfricanRecipe( "pizza", "30 minutes", "frying","nutritious")
print(African_pizza.prepare())
print(African_pizza.display_recipe())
Ethiopian_rice = EthiopianRecipe("ricre","2 hours","boiling","healthy")
print(Ethiopian_rice.prepare())
print(Ethiopian_rice.display_recipe())
Nigerian_pilau = NigerianRecipe( "pilau","45 minutes","One-pot","delicious")
print(Nigerian_pilau.prepare())
print(Nigerian_pilau.display_recipe())



#Q3
#**Wildlife Preservation:** You're a wildlife conservationist working on a
#program to track different species in a national park. Each species has its own
#characteristics and behaviors, such as its diet, typical lifespan, migration
#patterns, etc. Some species might be predators, others prey. You'll need to
#create classes to model `Species`, `Predator`, `Prey`, etc., and think about how
#these classes might relate to each other through inheritance.
class Animals:
    def __init__(self,diet,typical_lifespan,migration):
        self.diet=diet
        self.typical_lifespan=typical_lifespan
        self.migration=migration
    def track_species(self,species):
        print(f"{self}.__class.__.__{name}.__:{self.species}")    


class Predator(Animals):
    species="This animal is a canivirous"
class Prey(Animals):
    species="This animal is a herbivorous"    


    #Q3

class Species:
    def __init__(self, name, diet, lifespan, habitat):
        self.name = name
        self.diet = diet
        self.lifespan = lifespan
        self.habitat = habitat
    def display_information(self):
        return f"{self.name} is a {self.diet} with a lifespan of {self.lifespan} years."    
class Predator(Species):
    def __init__(self, name, diet, lifespan, habitat, hunting_style):
        super().__init__(name, diet, lifespan, habitat)
        self.hunting_style = hunting_style
class Prey(Species):
    def __init__(self, name, diet, lifespan, habitat, speed):
        super().__init__(name, diet, lifespan, habitat)
        self.speed=speed

    def display_information(self):
        super().display_information()
        print(f"speed:{self.speed}")    
lion = Predator("Lion", "Carnivore", 10, "Savannah", "Ambush")
gazelle = Prey("Gazelle", "Herbivore", 8, "Grasslands", 60) 
     


#Q4
#**African Music Festival:** You're in charge of organizing a Pan-African music
#festival. Many artists from different countries, each with their own musical style
#and instruments, are scheduled to perform. You need to write a program to
#manage the festival lineup, schedule, and stage arrangements. Think about how
#you might model the `Artist`, `Performance`, and `Stage` classes, and consider
#how you might use inheritance if there are different types of performances or
#stages.
class Artist:
    def __init__(self, name, country, musical_style, instruments):
        self.name = name
        self.country = country
        self.musical_style = musical_style
        self.instruments = instruments

    def __str__(self):
        return f"{self.name} from {self.country} plays {self.musical_style} on {self.instruments}"


class Performance:
    def __init__(self, artist, start_time, end_time, stage):
        self.artist = artist
        self.start_time = start_time
        self.end_time = end_time
        self.stage = stage

    def __str__(self):
        return f"{self.artist} performs at {self.stage} from {self.start_time} to {self.end_time}"


class Stage:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity

    def __str__(self):
        return f"{self.name} with capacity {self.capacity}"



artist_1 = Artist("Salif Keita", "Mali", "Wassoulou", ["kora", "balafon"])
artist_2 = Artist("Angelique Kidjo", "Benin", "Afrobeat", ["guitar", "vocals"])
artist_3 = Artist("Tinariwen", "Algeria", "Tassili n'Ajjer", ["guitar", "vocals"])

performance_1 = Performance(artist_1, "10:00 AM", "11:00 AM", Stage("Main Stage", 1000))
performance_2 = Performance(artist_2, "11:00 AM", "12:00 PM", Stage("World Stage", 500))
performance_3 = Performance(artist_3, "12:00 PM", "1:00 PM", Stage("Africa Stage", 250))

print(performance_1)
print(performance_2)
print(performance_3)


#Q5
#Create a class called Product with attributes for name, price, and quantity.
#Implement a method to calculate the total value of the product (price * quantity).
#Create multiple objects of the Product class and calculate their total values.
class Product:

    def __init__(self,name,price,quantity):
        self.name=name
        self.price=price
        self.quantity=quantity
    def total_value_product(self):
        total=(self.price*self.quantity)
product1=Product("bread",100,2) 
product2=Product("salt",20,3)
product3=Product("sugar",120,4)
total_value=Product(product1,product2,product3)




#Q6
#Implement a class called Student with attributes for name, age, and grades (a
#list of integers). Include methods to calculate the average grade, display the
#student information, and determine if the student has passed (average grade >=
#60). Create objects for the Student class and demonstrate the usage of these
#methods.
class Student:
    def __init__(self,name,age,grades):
        self.name=name
        self.age=age
        self.grades=grades 
    def calculate_average_grade(self):
        averageGrade>=60
        if len(self.grades)/2>=60:
            return f"{self.name} who is {self.age} has passed" 
        else:
            return f"{self.name} who is {self.age} has failed"       


#Q7
#Create a FlightBooking class that represents a flight booking system. Implement
#methods to search for available flights based on destination and date, reserve
#seats for customers, manage passenger information, and generate booking
#confirmations. 

class FlightBooking:
    def __init__(self,destination,date,reserve,seat_customers):
        self.destination=destination
        self.date=date
        self.reserve=reserve
        self.seat_customers=seat_customers
class FlightBooking:
    def __init__(self,flights):
        self.flights=[]
    def search_flights(self,destination,date):
            
        

 
#Q8
#Create a LibraryCatalog class that handles the cataloging and management of
#books in a library. Implement methods to add new books, search for books by
#title or author, keep track of available copies, and display book details.
class LibraryCatalog:

    def __init__(self,books,title,author):
        self.books=books
        self.title=title
        self.author=author
        self.cataloge=[]
   
    def add_book(self,new_book):
        for books in self.catalog:

            if self.books ==new_book:
                catalog.books.append(new_book)
                return catalog 
  


