# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 10:12:22 2020

@author: gateb
"""

class animaux:
    '''
    Cette class regroupe l'intégralité des animaux, au cas ou un animal
    n'est pas défini dans les class filles.
    elle sert à attribuer toutes les caractéristiques nécessaires
    d'un coup sans se repeter partout
    '''
    
    def __init__(self, nourriture, alimentation, nb_pattes):
        self.nourriture = nourriture
        self.nb_pattes = nb_pattes
        self.alimentation = alimentation
        
    def __str__(self):
        return  "Est un animal a " + self.nb_pattes + " pattes. Cet animal mange " +  self.nourriture +"g de nourriture par jour et est " + self.alimentation
            
class mammifere(animaux):
    '''
    Ma class 'mammifère' regroupe mes mammifères
    les attributs sont dans la class animal
    '''
    pass
    
class domestique(animaux):
    '''
    Ma class 'domestique' regroupe mes domestiques
    les attributs sont dans la class animal
    '''
    
    pass
    
class marin(animaux):
    '''
    Ma class 'marin' regroupe mes animaux marins
    les attributs sont dans la class animal
    mais on vient modifier le nombre de pattes car le smiens n'en ont pas
    '''
    
    def __init__(self, nourriture, alimentation, nb_pattes = 0):
        super().__init__(nourriture, nb_pattes, alimentation)
        self.nb_pattes = nb_pattes
        
    def __str__(self):
        return "Est un animal marin. Il ne possède pas de patte. Cet animal mange " + self. nourriture + "g de nourriture par jour et est " + self.alimentation
         
if __name__ == "__main__":
#    animal_1 = marin("200" , "Carnivore")
#    print(animal_1)
    '''
    Mon main est constitué d'un tableau
    qui met toutes les infos necessaire et me les affiches après
    '''
    print("_______________________________________________________________________________________")
    mon_zoo = {}
    mon_zoo["La Poule"] = domestique("200", "Omnivore", "4")
    mon_zoo["Le Serpent"] = animaux("200","Carnivore","0")
    mon_zoo["L'Autruche"] = animaux("1000", "Omnivore", "4")
    mon_zoo["L'Humain"] = mammifere("600", "Omnivore", "2")
    mon_zoo["La Pieuvre"] = marin("200", "Carnivore")
    mon_zoo["Le Crabe"] = marin("200", "Omnivore","8")
    
    '''
    requette est la question pour faire un petit affichage selon ce qu'on veut
    afficher. Plus pratique que de tout mettre d'un coup.
    '''
    
    requette = int(input("Que voulez vous faire ? (rentrez le nombre associé)\n 1- Voir l'état du Zoo.\n 2- Voir la nourriture a acheter par semaine.\n 3- Voir le nombre d'animaux marins.\n 4- Pour voir le nombre de pattes dans le Zoo.\n 5- Voir le nombre d'animaux Omnivore\n "))
    
    if requette == 1:
        for my_key in mon_zoo:
            print(my_key + " " + str(mon_zoo[my_key]))
            print("_______________________________________________________________________________________")
            
    if requette == 2:
        nr_semaine = 0
    
        for my_key in mon_zoo:
        
            print(my_key + " " + str(mon_zoo[my_key].nourriture))
            print("_______________________________________________________________________________________")
            nr_semaine = nr_semaine + int(mon_zoo[my_key].nourriture)
    
        print("Le zoo doit acheter, par semaine, "+ str(nr_semaine * 7) + "g de nourriture")
        
    if requette == 3:
        
        count = 0
        
        for my_key in mon_zoo:
            
            if (isinstance(mon_zoo[my_key], marin) == 1):
                count += 1
                
        print("Nous avons " + str(count) + " Animal/Animaux dans notre Zoo.")
        
    if requette == 4:
        
        pattes = 0
         
        for my_key in mon_zoo:
            pattes = pattes + int(mon_zoo[my_key].nb_pattes)
            
        print("Il y a " + str(pattes) + " pattes au total dans le Zoo.")

    if requette == 5:
        
        count = 0

        for my_key in mon_zoo:
            
            if (mon_zoo[my_key].alimentation == "Omnivore"):
                count = count + 1

        print("Il y a " + str(count) + " animal/animaux omnivores dans le zoo")
        
    else : 
        print("Merci de votre visite ! Et à bientôt !")
        