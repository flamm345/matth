#!/usr/bin/python
# -*- coding: utf-8 -*-
import random
import logging

logger = logging.getLogger("calcul2")


class Query:
    """ Root Class - defined  the overall functionality"""
    query = ""
    answerType = "Int"
    correctAnswer = 0
    currentAnswer = -1
    point = 0
    answerMessage = "pas de reponse ..:"

    def __init__(self):
        pass

    def isCorrect(self):
        if self.currentAnswer == self.correctAnswer:
            return True
        else:
            return False

    def setCurrentAnswer(self, answer):
        self.currentAnswer = answer
        if self.isCorrect():
            self.point = 1
            self.answerMessage = "Bonne réponse"
        else:
            self.point = 0
            self.answerMessage = "Mauvaise reponse - le resultat est " + \
                                 str(self.correctAnswer)

    @staticmethod
    def getQueryInstance(queryType=None):
        if queryType is None:
            choix = random.randint(1, 4)
            if choix == 1:
                m = QueryAdd()
            elif choix == 2:
                m = QueryAdd2()
            elif choix == 3:
                m = QueryMinus()
            else:
                m = QueryMinus2()
            return m
        else:
            return None


class QueryAdd (Query):
    """ Add a number to Another and ask the result"""

    def __init__(self, xRange=(7, 8), yRange=(1, 50)):
        logger.debug("init QueryAdd function...")
        x = random.randint(1, 50)
        y = random.randint(7, 8)
        queryString = [str(x), " + ", str(y), " = "]
        self.query = "".join(queryString)
        self.correctAnswer = x + y


class QueryAdd2 (Query):
    def __init__(self):
        logger.debug("init QueryAdd2 function...")
        x = random.randint(7, 8)
        y = random.randint(1, 50)
        if x <= y:
            queryString = [str(x), " + ? = ", str(y), "      ? = "]
            self.correctAnswer = y - x
        else:
            queryString = [" ? + ", str(y), " = ", str(x), "     ? = "]
            self.correctAnswer = x - y
        self.query = "".join(queryString)


class QueryMinus (Query):
    def __init__(self):
        x = random.randint(20, 50)
        y = random.randint(7, 8)
        queryString = [str(x), " - ", str(y), " = "]
        self.query = "".join(queryString)
        self.correctAnswer = x - y


class QueryMinus2(Query):
    def __init__(self):
        x = random.randint(1, 50)
        y = random.randint(1, 50)
        if x >= y:
            queryString = [str(x), " - ? = ", str(y), "      ? = "]
            self.correctAnswer = x - y
        else:
            queryString = [" ? - ", str(x), " = ", str(y), "     ? = "]
            self.correctAnswer = x + y
        self.query = "".join(queryString)

if __name__ == '__main__':
    m = QueryMinus2()
    print m.query
    resp = int(raw_input("my answer: "))
    m.setCurrentAnswer(resp)
    print "anwser : %s " % (m.isCorrect())
    print m.point
