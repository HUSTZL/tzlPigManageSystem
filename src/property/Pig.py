

class Pig():

    def __init__(self, PigId, Type, Weight, Age, IsSick, FarmId):
        self.__pigId = PigId
        self.__type = Type
        self.__weight = Weight
        self.__age = Age
        self.__isSick = IsSick
        self.__farmId = FarmId
        return

    @property
    def pigId(self):
        return self.__pigId

    @property
    def type(self):
        return self.__type

    @property
    def weight(self):
        return self.__weight

    @property
    def isSick(self):
        return self.__isSick

    @property
    def farmId(self):
        return self.__farmId

    @pigId.setter
    def pigId(self, n):
        self.__pigId = n

    @type.setter
    def type(self, n):
        self.__type = n

    @weight.setter
    def weight(self, n):
        self.__weight = n

    @isSick.setter
    def isSick(self, n):
        self.__isSick = n

    @farmId.setter
    def farmId(self, n):
        self.__farmId = n

    def __str__(self):
        return 'Pig [Id={} , Type={}, Age={}, IsSick={}, FarmId={}, Weight={}]'.format(self.__pigId, self.__type, self.__age, self.__isSick, self.__farmId, self.__weight)