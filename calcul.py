#!/usr/bin/python

import random 
import sys
import time

nb_questions = 20 
maxTime = 150 # en secondes
start_time = time.time()
print ""
print 80*'-'
print "hello Matthieu - c'est ton programme de math .. :)"
print 80*'-'
print 
point = 0
for i in range (1,(nb_questions+1)) : 
	x = random.randint(1,19) 
	y = random.randint(11,19)
 	rep = raw_input("Question %s :               %s + %s =  " % (i,x,y))	
	if rep is None or rep == "" : 
		rep = 0 
	end_time = time.time()
	diff = end_time - start_time
	if (diff > maxTime) :
		print ("Temps Ecoule")
		break
	if (int(rep) == (x + y )) : 
		print "    BONNE REPONSE"
		point = point + 1
	else: 
		print "    MAUVAISE reponse"	

print "-----------------------------"
print "| temps passe " 
print (diff)
print "| Ta note est de %s sur %s " % (point , nb_questions)
print "-----------------------------"

