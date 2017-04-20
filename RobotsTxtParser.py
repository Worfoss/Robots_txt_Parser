# -*- coding: utf-8 -*-
# Python v3.6

from robots import Robots

url = 'https://www.google.com'

robot = Robots(url)
robot.urlParser(robot.getRobots())
for u in robot.useragents:
    for d in u.disallow:
        print(robot.url+d+" : "+str(robot.getCodeOf(d)))
    for a in u.allow:
        print(robot.url+a+" : "+str(robot.getCodeOf(a)))
