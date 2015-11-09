#!/usr/bin/python

import random 
import sys
import time

nb_questions = 20 
maxTime = 60 # en secondes
start_time = time.time()
print ""
print 80*'-'
print "hello Matthieu - c'est ton nouveau programme de math .. :)"
print 80*'-'
print 
point = 0
typequestions = ['unite', 'dizaine', 'centaine']
for i in range (1,(nb_questions+1)) : 
	centaine  = random.randint(0,9) 
	dizaine  = random.randint(0,9) 
	unite  = random.randint(0,9)
	
	typequestion = typequestions[random.randint(0,2)]

 	rep = raw_input("Question %s :     Quelle est la %s dans le nombre suivant : %s%s%s " % (i,typequestion,centaine,dizaine,unite))	
	if rep is None or rep == "" : 
		rep = 0 
	end_time = time.time()
	diff = end_time - start_time
	if (diff > maxTime) :
		print ("Temps Ecoule")
		break
        if (typequestion == 'centaine'):
		if (int(rep) == centaine):
			print "    BONNE REPONSE"
			point = point + 1
		else: 
			print "    MAUVAISE reponse"	
	elif (typequestion == 'dizaine'):
		if (int(rep) == dizaine):
			print "    BONNE REPONSE"
			point = point + 1
		else: 
			print "    MAUVAISE reponse"	
	else :
		if (int(rep) == unite) : 
			print "    BONNE REPONSE"
			point = point + 1
		else: 
			print "    MAUVAISE reponse"	

print "-----------------------------"
print "| temps passe " 
print (diff)
print "| Ta note est de %s sur %s " % (point , nb_questions)
print "-----------------------------"

