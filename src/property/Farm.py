

class Farm():

    def __init__(self, FarmId, Remain):
        self.__FarmId = FarmId
        self.__Remain = Remain
        return

    @property
    def FarmId(self):
        return self.__FarmId

    @property
    def Remain(self):
        return self.__Remain

    @FarmId.setter
    def FarmId(self, n):
        self.__FarmId = n

    @Remain.setter
    def Remain(self, n):
        self.__Remain = n

    def __str__(self):
        return 'Farm [Id={} , Remain={}]'.format(self.__FarmId, self.__Remain)
