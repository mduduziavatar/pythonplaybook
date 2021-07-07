class Person:
    def __init__(self, name, age, email, password):
        self.name = name
        self.age = age
        self.email = email
        self.password = password
name = input(str('Enter Username'))
age = input(str("Enter your age"))
email = input(str("Enter your email"))
password = input(str("Enter your password"))

person = Person(name, age, email, password)
print(person.name)
print(person.age)
print(person.email)
print(person.password)