class Useragent:
    def __init__(self, name):
        self.__name = name
        self.__allow = []
        self.__disallow = []

    #GETTER
    @property
    def name(self):
        return self.__name

    @property
    def allow(self):
        return self.__allow

    @property
    def disallow(self):
        return self.__disallow

    #SETTER
    @allow.setter
    def allow(self, link):
        self.__allow.append(link)

    @disallow.setter
    def disallow(self, link):
        self.__disallow.append(link)
