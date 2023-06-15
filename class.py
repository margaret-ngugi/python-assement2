#Q1
#**Ancestral Stories:** In many African cultures, the art of storytelling is passed
#down from generation to generation. Imagine you're creating an application that
#records these oral stories and translates them into different languages. The
#stories vary by length, moral lessons, and the age group they are intended for.
#Think about how you would model `Story`, `StoryTeller`, and `Translator`
#objects, and how inheritance might come into play if there are different types of
#stories or storytellers.

#1. inputs,length,moral_lesson,age
#2. process ,creating a class and passing attributes in the function constructor,adding methods
#3.output,records of oral stories and translates into different languages
class OralStories:
    def __init__(self,length,moral_lesson,age_group):
        self.length=length
        self.moral_lesson=moral_lesson
        self.age_proup=age_group

    def record_story(self,story):
        if self.length<50 and self.moral_lesson="obedient" and self.age_group<15:
            return f"this {story} is recorded for children"
        elif self.length>50 and self.moral_lesson="hardworking" and self.age_group>15:
            return f"this {story} is recorded for students" 
        else:
            return return f"this {story} is recorded for adults" 

    def translate_story(self,languages):
        if self.length<50 and self.moral_lesson="obedient" and self.age_group<15:
            return f"this {story} is tranlated to kiswahili"
        elif self.length>50 and self.moral_lesson="hardworking" and self.age_group>15:
            return f"this {story} is translated to English" 
        else:
            return return f"this {story} istranslated to mother tongue" 

            



#Q2        
#**African Cuisine:** You're creating a recipe app specifically for African cuisine.
#The app needs to handle recipes from different African countries, each with its
#unique ingredients, preparation time, cooking method, and nutritional
#information. Consider creating a `Recipe` class, and think about how you might
#create subclasses for different types of recipes (e.g., `MoroccanRecipe`,
#EthiopianRecipe`, `NigerianRecipe`), each with their own unique properties and
#methods. 
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
     


#Q4
#**African Music Festival:** You're in charge of organizing a Pan-African music
#festival. Many artists from different countries, each with their own musical style
#and instruments, are scheduled to perform. You need to write a program to
#manage the festival lineup, schedule, and stage arrangements. Think about how
#you might model the `Artist`, `Performance`, and `Stage` classes, and consider
#how you might use inheritance if there are different types of performances or
#stages.
class MusicFestival:
    def __init__(self,lineup,schedule,stage_arrangements):
        self.lineup=lineup
        self.schedule=schedule
        self.stage_arrangements=stage_arrangements







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
print(total_value.total_value_product())



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
            return f"{self.name} who is {self.age} has failed""       


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
            if self.books == new_books:
                catalog.books.append(new_book)
                return catalog
    def search_books(self):


