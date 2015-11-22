#!/usr/bin/python
# -*- coding: utf-8 -*-

import time
import calculQueries
import random
import logging
from logging.handlers import RotatingFileHandler

# -- initialisation du logging
logger = logging.getLogger("calcul")
logger.setLevel(logging.DEBUG)
formater = logging.Formatter('%(asctime)s :: %(levelname)s :: %(message)s')
streamHandler = RotatingFileHandler('activity.log', 'a', 1000000, 1)
streamHandler.setFormatter(formater)
streamHandler.setLevel(logging.DEBUG)
logger.addHandler(streamHandler)

logger.debug("")
nb_questions = 20
logger.debug("nb_questions = %s ", nb_questions)
maxTime = 180   # en secondes
start_time = time.time()
print ""
print 80*'-'
print "hello Matthieu - c'est ton programme de math .. :) "
print 80*'-'
print

point = 0
for i in range(1, (nb_questions+1)):
    logger.debug("Question %s", i)
    choix = random.randint(1, 3)
    if choix == 1:
        logger.debug("choix %s : QueryAdd", choix)
        m = calculQueries.QueryAdd()
        logger.debug(m)
    elif choix == 2:
        logger.debug("choix %s : QueryAdd2", choix)
        m = calculQueries.QueryAdd2()
        logger.debug(m)
    else:
        logger.debug("choix %s : QueryMinus2", choix)
        m = calculQueries.QueryMinus2()
        logger.debug("fin du choix : %s", m)
    logger.debug("%s", m.query)
    rep = raw_input(m.query)
    m.setCurrentAnswer(int(rep))
    end_time = time.time()
    diff = end_time - start_time
    print m.answerMessage
    if (diff > maxTime):
        print ("Temps Ecoule")
        break
        print m.answerMessage
    point = point + m.point

print "-----------------------------"
print "| temps passe "
print (diff)
print "| Ta note est de %s sur %s " % (point, nb_questions)
print "-----------------------------"
