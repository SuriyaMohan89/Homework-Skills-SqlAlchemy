"""

This file is the place to write solutions for parts two and three of skills-
sqlalchemy. Remember to consult the exercise instructions for more complete
explanations of the assignment.

All classes from model.py are being imported for you here, so refer to classes
by just their class name (not model.ClassName).

"""

from model import *

init_app()

# -----------------
# PART TWO: QUERIES
# -----------------

# # Get the human with the id 2.
# q1 = Human.query.get(2)
# print q1

# # Get the *first* animal with the species 'fish'
# q2 = Animal.query.filter(Animal.animal_species =='fish').first()
# print q2
# # Get all of the animals for the human with the id 5 and the animal species 'dog'

# q3 = Animal.query.filter(Human.human_id == 5, Animal.animal_species == "dog").first()
# print q3


# # # Get all the animals that were born after 2015 (do not include animals without birth years).
# q4 = Animal.query.filter(Animal.birth_year > 2015, Animal.birth_year != None).all()
# print q4

# # Find the humans with first names that start with 'J'


# q5 = Human.query.filter(Human.fname.like('%J%')).all()

# print q5

# # Find all the animals without birth years in the database.
# q6 = Animal.query.filter(Animal.birth_year == None).all()
# print q6

# # # Find all animals that are either fish or rabbits
# q7 = Animal.query.filter((Animal.animal_species == 'fish') | (Animal.animal_species == 'rabbits')).all()
# print q7


# # Find all the humans whose email addresses do not contain 'gmail'
# q8 = Human.query.filter(Human.email.like('%gmail%')).all()
# print q8

# # ---------------------
# PART THREE: FUNCTIONS
# ---------------------

# ***Do not use more than one query for each function***

# 1. Write a function, print_directory, which does not take any arguments
#    and prints out each human (once) with a list of their animals.

#    The output should look like this (with tabs to indent each animal name under
#    a human's name)

#       Human_first_name Human_last_name
#           Animal name (animal species)
#           Animal name (animal species)
#
#       Human_first_name Human_last_name
#           Animal name (animal species)

def print_directory():
    """ Prints out Each Human with a list of their animals"""
    # owners = Human.query.options(db.joinedload('animals.human')).order_by(Human.human_id).all()

    # for owner in owners:
    # 	print owner.fname,owner.lname
    # 	pets = Animal.query.filter(owner.human_id == Animal.human_id).all()
    # 	for pet in pets:
    # 		print '\t'+pet.name +'('+ pet.animal_species +')'

    owners = Human.query.options(db.joinedload('pets')).order_by(Human.human_id).all()
    for owner in owners:
    	print owner.fname
    	for pet in owner.pets:
    		print '\t{name} ({species})'.format(name=pet.name, species=pet.animal_species)
    

    	# if owner.human_id == Animal.human_id :

    	# 	print Animal.owner.name
    	 

    




print_directory()

# 2. Write a function, get_animals_by_name, which takes in a string representing
#    an animal name (or part of an animal name) and *returns a list* of Animal
#    objects whose names contain that string.

def get_animals_by_name(name):
    """ Returns a List of animal objects contain the string passed as argument"""

    pet = Animal.query.filter(Animal.name.like('%{}%'.format(name))).all()
    print pet

get_animals_by_name("Fluff")

# 3. Write a function, find_humans_by_animal_species, which takes in an animal
#    species and *returns a list* of all of Human objects who have animals of
#    that species.
def find_humans_by_animal_species(species):
    """Returns a list of Human objects who have animals of that species"""
    owner_list = []
    pet_owner= Animal.query.filter(Animal.animal_species == '{}'.format(species)).order_by(Animal.human_id).distinct(Animal.human_id).all()

   
    for pet in  pet_owner:
    	owner_list.append(pet.owner)

    print owner_list

  
find_humans_by_animal_species('dog')











