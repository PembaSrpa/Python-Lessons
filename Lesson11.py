# create a 2D vector class and use it to create another class representing a 3D vector
class vector2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"vector2D(x={self.x}, y={self.y})"

class vector3(vector2):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z

    def __repr__(self):
        return f"vector3D(x={self.x}, y={self.y}, z={self.z})"
    
# Example usage
v2 = vector2(3, 4)
print(v2)                    

v3 = vector3(1, 2, 2)
print(v3)            


# create a class Pets from a class Animals and further create class Dogs from Pets. Add a method back to class Dogs
class Animals:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        return f"{self.name} makes a sound"

class Pets(Animals):
    def __init__(self, name, owner):
        super().__init__(name)
        self.owner = owner
    
    def speak(self):
        return f"{self.name} is a pet of {self.owner}"

class Dogs(Pets):
    def __init__(self, name, owner, breed):
        super().__init__(name, owner)
        self.breed = breed
    
    def bark(self):
        return f"{self.name} barks: Woof! Woof!"

# Example usage
dog = Dogs("Buddy", "John", "Golden Retriever")
print(dog.speak())
print(dog.bark())

#create a class Employee and add salary and increment property to it. Write a SalaryAfterIncrement method with a @property decorator with a setter which changes the value of increment based on salary
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        self._increment = 0

    @property
    def increment(self):
        return self._increment

    @increment.setter
    def increment(self, value):
        self._increment = value

    def salary_after_increment(self):
        return self.salary + self.increment

# Example usage
emp = Employee("Alice", 50000)
emp.increment = 5000
print(f"{emp.name}'s salary after increment: {emp.salary_after_increment()}")

#write a class Complex to represent complex numbers and add and multiply two complex numbers using operator overloading
class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)

    def __mul__(self, other):
        real_part = self.real * other.real - self.imag * other.imag
        imag_part = self.real * other.imag + self.imag * other.real
        return Complex(real_part, imag_part)

    def __repr__(self):
        return f"{self.real} + {self.imag}i"
# Example usage
c1 = Complex(2, 3)
c2 = Complex(4, 5)
c3 = c1 + c2
c4 = c1 * c2
print(f"Addition: {c3}")
print(f"Multiplication: {c4}")

#create a class vector representing a 3D vector and overload the + and * operators to add and multiply two vectors
class Vector3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        return Vector3D(self.x + other.x, self.y + other.y, self.z + other.z)

    def __mul__(self, other):
        return (self.x * other.x) + (self.y * other.y) + (self.z * other.z)

    def __repr__(self):
        return f"Vector3D(x={self.x}, y={self.y}, z={self.z})"
# Example usage
v1 = Vector3D(1, 2, 3)
v4 = Vector3D(4, 5, 6)
v5 = v1 + v4
dot_product = v1 * v4
print(f"Vector Addition: {v5}")
print(f"Dot Product: {dot_product}")

# write __str__() method to print the vector as 7i + 8j + 9k
class Vector3DStr:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f"{self.x}i + {self.y}j + {self.z}k"
# Example usage
v = Vector3DStr(7, 8, 9)
print(v)

# __repr__() vs __str__()
class Sample:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f"Sample(value={self.value})"

    def __str__(self):
        return f"Sample with value: {self.value}"
# Example usage
s = Sample(10)
print(repr(s))  # Calls __repr__()
print(str(s))   # Calls __str__()

# override __len__() method to return the length of the vector3d
class Vector3DLen:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __len__(self):
        return int((self.x**2 + self.y**2 + self.z**2) ** 0.5)
# Example usage
v_len = Vector3DLen(3, 4, 12)
print(f"Length of vector: {len(v_len)}")