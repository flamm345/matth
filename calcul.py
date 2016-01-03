#!/usr/bin/python
# -*- coding: utf-8 -*-

import time
import calculQueries
import logging
from logging.handlers import RotatingFileHandler

# -- initialisation du logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
formater = logging.Formatter('%(asctime)s :: %(levelname)s :: %(message)s')
streamHandler = RotatingFileHandler('activity.log', 'a', 1000000, 1)
streamHandler.setFormatter(formater)
streamHandler.setLevel(logging.DEBUG)
logger.addHandler(streamHandler)


def welcomeMsg():
    print ""
    print 80*'-'
    print "hello Matthieu - c'est ton programme de math .. :) "
    print 80*'-'
    print

def callQuery():
    m = calculQueries.Query.getQueryInstance()
    logger.debug(m)
    logger.debug("%s", m.query)

    while True:
        try:
            rep = int(raw_input(m.query))
            break
        except ValueError:
            print"Ooops - ce n'est pas un nombre..:("



    m.setCurrentAnswer((rep))
    return m


if __name__ == "__main__":
    welcomeMsg()

    nb_questions = 20

    logger.debug("nb_questions = %s ", nb_questions)
    maxTime = 180   # en secondes
    start_time = time.time()

    point = 0

for i in range(1, (nb_questions+1)):
    logger.debug("Question %s", i)
    m = callQuery()
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
