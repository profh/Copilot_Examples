# create a list of 100 numbers
# numbers = list(range(1, 101))  ## <press control-enter to see all suggestions>
numbers = [i for i in range(1, 101)]  # choosing a different suggestion

# print the list
print(numbers)

# deducing the function from the name
def get_even_numbers(numbers):
    even_numbers = []
    for number in numbers:
        if number % 2 == 0:
            even_numbers.append(number)
    return even_numbers
  
even_numbers = get_even_numbers(numbers)
odd_numbers = [i for i in numbers if i not in even_numbers]


# Using copilot to create classes
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def get_name(self):
        return self.name
    def get_age(self):
        return self.age

    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")
        
# a list of 10 people
PEOPLE = [
    Person("John", 20),
    Person("Jane", 22),
    Person("Alice", 16),
    Person("Bob", 21),
    Person("Jack", 15),
    Person("Jill", 24),
    Person("Mike", 19),
    Person("Mary", 18),
    Person("Harry", 27),
    Person("Liz", 26),
]

# print greeting for all people in PEOPLE list
for person in PEOPLE:
    person.greet()

# filter people by age
adults = [person for person in PEOPLE if person.get_age() > 18]
for adult in adults:
    print(adult.get_name())  