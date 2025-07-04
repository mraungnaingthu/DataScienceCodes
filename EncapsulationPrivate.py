class Student:
    def __init__(self, name, useremail, password):
        self.name = name
        self.__useremail = useremail  # Private attribute
        self.__password = password   # Private attribute

    def getUser(self):  # Adding a method to access private attributes
        return self.__useremail, self.__password

class Admin(Student):
    def setUser(self, useremail, password):
        self.__useremail = useremail  # Updating private attributes
        self.__password = password

    def getUser(self):
        return self.__useremail, self.__password  # Accessing private attributes

# Correct instantiation
user1 = Student("Aung Naing Thu", "aungnaingthu@gmail.com", "Aung123")

# Checking the user's details using a method
print(user1.getUser())
