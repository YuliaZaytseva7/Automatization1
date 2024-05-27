class User:
    
    def __init__(self,first_name, last_name):
        self.name = first_name
        self.surname = last_name
    
    def printName(self):
        print("Имя", self.name)

    def printSurname(self):
        print("Фамилия", self.surname)

    def printAll(self):
        print("Имя и фамилия", self.name, self.surname)
    
