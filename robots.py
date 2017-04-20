# -*- coding: utf-8 -*-
# Python v3.6

from urllib.request import urlopen
from useragent import Useragent
import urllib.error
import sys
import re

class Robots:
    def __init__(self, url):
        self.__url = url
        self.__useragent = []

    #GETTER
    @property
    def url(self):
        return self.__url

    @property
    def useragents(self):
        return self.__useragent

    @property
    def useragent(self, index):
        if len(self.__useragent) < index:
            return self.__useragent[index]   

    #SETTER
    @useragent.setter
    def useragent(self, useragent):
        if self.getIndexOfUseragent(useragent) == -1:
            self.__useragent.append(Useragent(useragent))
    
    #METHODE
    def getIndexOfUseragent(self, name):
        index = -1
        for i in range(0, len(self.useragents)):
            if self.useragents[i].name == name:
                index = i
        return index

    def getUseragentNamed(self, name):
        return self.useragents[self.getIndexOfUseragent(name)]

    def getAllUseragentName(self):
        result = []
        for u in self.useragents:
            result.append(u.name)
        return result

    def getRobots(self):
        try:
            html = urlopen(self.url + '/robots.txt' )
            result = html.read().decode()
        except IOError:
            sys.exit("** There is no robots.txt for : " + self.url) 
        print('** Robots.txt find for : ' + self.url + '\n')
        return result

    def urlParser(self, page):
        currentUA = None
        page = re.findall(r'(.*)\n', page)
        for line in page:
            uAgent = re.search(r'^User-agent: (.*)$', line)
            uDisallow = re.search(r'^Disallow: (.*)$', line)
            uAllow = re.search(r'^Allow: (.*)$', line)
            if uAgent:
                self.useragent = uAgent.group(1)
                currentUA = uAgent.group(1)
            if uDisallow:
                self.getUseragentNamed(currentUA).disallow.append(uDisallow.group(1))
            if uAllow:
                self.getUseragentNamed(currentUA).allow.append(uAllow.group(1))

    def getCodeOf(self, path):
        result = None
        try:
            connect = urllib.request.urlopen(self.url + path)
        except urllib.error.HTTPError as e:
            result = e.code
        except urllib.error.URLError as e:
            result = 'URLError'
        else:
            result = connect.getcode()
        return result

