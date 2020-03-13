# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 09:37:18 2020

@author: gateb
"""
import datetime
import random
import json

class Animal:
    '''
    Class mere, toutes les class filles héritent des attribut de cette class
    '''
    
    def __init__(self, name, year, month, day):
        self.name = name
        self.year = year
        self.day = day
        self.month = month
        
        self.age = datetime.datetime(year = year, month = month, day = day)
        self.sexe = random.choice(["Mâle", "Femelle"])
        
        
    def __str__(self):
        return  "Un(e) " + str(self.name) + ". Il est né en " +  str(self.age) +"  et c'est un(e) " + str(self.sexe)
            
class Farm:
    
    def __init__(self, name):
        
        self.name = name
        self.Farm_animals = []
        
#    def __init__(self, name, json_string):
#        
#        pass

        
    def __str__(self):
        
        out = "Nous avons dans cette Ferme :\n"
        
        for my_key in self.Farm_animals:
            
            out += str(my_key) +"\n"
            out += "_______________________________________________________________________________________"
        
        return out        
    
    
if __name__ == "__main__":
    date_farm = datetime.datetime(year = 2020, month = 1, day = 1)
    
    Farm_list = []
    Farm_list.append(Farm("Vide"))
    Farm_list.append(Farm("Première ferme"))
    Farm_list.append(Farm("Deuxième ferme"))
#    Farm_list.append(Farm("Deuxième ferme", json string)
    Farm_list[1].Farm_animals.append(Animal("Mouton", 2020, 3, 5))
    Farm_list[1].Farm_animals.append(Animal("Poule", 2020, 3, 5))
    Farm_list[2].Farm_animals.append(Animal("Serpent", 2020, 3, 5))
    Farm_list[2].Farm_animals.append(Animal("Serpent", 2020, 3, 5))
    
    requette = int(input("Quelle Ferme voulez vous visiter ? :\n"))
#    print(Farm_list[requette])
    
    my_delta = datetime.timedelta(weeks = 0, days = 30, hours = 0, seconds = 0)
    
    i = 0
    while i < 20:
        Farm_list[1].Farm_animals[0].age = Farm_list[1].Farm_animals[0].age + my_delta
        i += 1
        
    if int(Farm_list[1].Farm_animals[0].age.year) - int(date_farm.year) >= 1:
        Farm_list[1].Farm_animals.append(Animal("Poule", 2020, 3, 5))
        
        
    print(Farm_list[requette])