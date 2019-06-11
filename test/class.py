class My:
    def __init__(self, info):
        self.name = info["name"]
        self.user = "123"
        self.info = info

    def __repr__(self):
        return str(self["info"])

    def __str__(self):
        return self.__repr__()


my = My({'name': "hoang"})
print(my)