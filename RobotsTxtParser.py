# -*- coding: utf-8 -*-
# Python v3.6

from robots import Robots
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-u', '--url', help='Input file',
                    metavar="Firewall rule's file to parse")
parser.add_argument('--xml', help='Input file',
                    metavar="Firewall rule's file to parse")
parser.add_argument('--csv', help='Input file',
                    metavar="Firewall rule's file to parse")
args = parser.parse_args()

def errorFiller(currentCode, currentUrl, error):
    if currentCode and currentUrl:
        if not currentCode in list(error.keys()):
            error.update({currentCode:[currentUrl]})
        else:
            error[currentCode].append(currentUrl)

def errorsFiller(useragent, error):
    for u in robot.useragents:
        currentCode = None
        currentUrl = None 
        
        for d in u.disallow:
            currentUrl = robot.url + d
            currentCode = robot.getCodeOf(d)
            errorFiller(currentCode, currentUrl, error)
        for a in u.allow:
            currentUrl = robot.url + a
            code = robot.getCodeOf(a)
            errorFiller(currentCode, currentUrl, error)   

def getKey(error):
    key = list(error.keys())
    key.sort()
    return key

def xmlOutput(error, output):
    print('xml')

def csvOutput(error, output):
    print('csv')

def printError(error):
    key = getKey(error) 
    for e in key:
        print('\n-----__' + str(e)  + '__-----')
        for u in error[e]:
            print(u)


url = args.url
xml = args.xml
csv = args.csv
robot = Robots(url)
error = {}

robot.urlParser(robot.getRobots())
errorsFiller(robot.useragents, error)

printError(error)

