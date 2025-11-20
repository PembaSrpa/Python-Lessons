#create a class programmer for storing information about programmers
class Programmer:
    def __init__(self, name, age, languages):
        self.name = name
        self.age = age
        self.languages = languages

#class calculator for finding square and square root of a number
class Calculator:
    @staticmethod
    def greet(name):
        return "Welcome to the Calculator!"+", " + name
    
    @staticmethod
    def square(number):
        return number * number

    @staticmethod
    def square_root(number):
        return number ** 0.5

#create a class attribute a ; create an object from it and set a directly using object a = 0.Does this change the class attribute?
class Example:
    a = 5

#write a class train which has methods to book a ticket , get status of the train and get fare information
class Train:
    def __init__(self, name, fare):
        self.name = name
        self.fare = fare
        self.booked_tickets = 0

    def book_ticket(self):
        self.booked_tickets += 1
        return f"Ticket booked successfully! Total booked tickets: {self.booked_tickets}"

    def get_status(self):
        return f"Train Name: {self.name}, Booked Tickets: {self.booked_tickets}"

    def get_fare_info(self):
        return f"Fare for the train {self.name} is: {self.fare}"
    
#can you change the self parameter inside a class to something else? Try it out.
class CustomSelf:
    def __init__(custom, value):
        custom.value = value

    def display(custom):
        return f"Value is: {custom.value}"
    
    
#example usage
if __name__ == "__main__":
    #create a programmer object
    prog = Programmer("Alice", 30, ["Python", "Java", "C++"])
    print(f"Programmer Name: {prog.name}")
    print(f"Programmer Age: {prog.age}")
    print(f"Programming Languages: {', '.join(prog.languages)}")

    #use calculator to find square and square root
    num = 16
    print(Calculator.greet("User"))
    print(f"Square of {num} is {Calculator.square(num)}")
    print(f"Square root of {num} is {Calculator.square_root(num)}")
    
    #demonstrate class attribute behavior
    print(f"Initial class attribute a: {Example.a}")
    obj = Example()
    obj.a = 0
    print(f"Object attribute a after setting obj.a = 0: {obj.a}")
    print(f"Class attribute a remains unchanged: {Example.a}")
    
    #create a train object and use its methods
    train = Train("Express Line", 50)
    print(train.book_ticket())
    print(train.get_status())
    print(train.get_fare_info())
    
    #demonstrate changing self parameter
    custom_obj = CustomSelf(10)
    print(custom_obj.display())