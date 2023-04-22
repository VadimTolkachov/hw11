class Name:
    def __init__(self, name) -> None:
        self.__name = None
        self.name = name
        

    @property
    def name(self):
        return str(self.__name)
    
    @name.setter
    def name(self, name:str):
        if name[0].islower():
            raise KeyError()
        self.__name = name


a = Name('vadim')
print(a.name)
        

    