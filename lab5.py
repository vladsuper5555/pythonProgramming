import math

class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must implement this method.")

    def perimeter(self):
        raise NotImplementedError("Subclasses must implement this method.")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        area = math.pi * self.radius ** 2
        print(f"Circle area: {area:.2f}")
        return area

    def perimeter(self):
        perimeter = 2 * math.pi * self.radius
        print(f"Circle perimeter: {perimeter:.2f}")
        return perimeter

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        area = self.width * self.height
        print(f"Rectangle area: {area}")
        return area

    def perimeter(self):
        perimeter = 2 * (self.width + self.height)
        print(f"Rectangle perimeter: {perimeter}")
        return perimeter

class Triangle(Shape):
    def __init__(self, side_a, side_b, side_c):
        self.a = side_a
        self.b = side_b
        self.c = side_c

    def area(self):
        # Using Heron's formula
        s = self.perimeter() / 2
        area = math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))
        print(f"Triangle area: {area:.2f}")
        return area

    def perimeter(self):
        perimeter = self.a + self.b + self.c
        print(f"Triangle perimeter: {perimeter}")
        return perimeter


class Account:
    def __init__(self, account_number, balance=0.0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ${amount:.2f}. Current balance: ${self.balance:.2f}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Withdrawal denied. Insufficient funds.")
        else:
            self.balance -= amount
            print(f"Withdrew ${amount:.2f}. Current balance: ${self.balance:.2f}")

    def display_balance(self):
        print(f"Account {self.account_number} balance: ${self.balance:.2f}")

class SavingsAccount(Account):
    def __init__(self, account_number, balance=0.0, interest_rate=0.02):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        interest = self.balance * self.interest_rate
        print(f"Interest accrued: ${interest:.2f}")
        return interest

class CheckingAccount(Account):
    def __init__(self, account_number, balance=0.0, overdraft_limit=500.0):
        super().__init__(account_number, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount > self.balance + self.overdraft_limit:
            print("Withdrawal denied. Overdraft limit exceeded.")
        else:
            self.balance -= amount
            print(f"Withdrew ${amount:.2f}. Current balance: ${self.balance:.2f}")



class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

class Car(Vehicle):
    def calculate_mileage(self, miles_driven, gallons_used):
        mileage = miles_driven / gallons_used
        print(f"Car mileage: {mileage:.2f} MPG")
        return mileage

class Motorcycle(Vehicle):
    def calculate_mileage(self, miles_driven, gallons_used):
        mileage = miles_driven / gallons_used
        print(f"Motorcycle mileage: {mileage:.2f} MPG")
        return mileage

class Truck(Vehicle):
    def __init__(self, make, model, year, towing_capacity):
        super().__init__(make, model, year)
        self.towing_capacity = towing_capacity

    def calculate_towing_capacity(self):
        print(f"Towing capacity: {self.towing_capacity} lbs")
        return self.towing_capacity



class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def perform_duties(self):
        print(f"{self.name} is performing general duties.")

class Manager(Employee):
    def __init__(self, name, salary):
        super().__init__(name, salary)
        self.list_of_employees = set()

    def add_employee(self, employee):
        self.list_of_employees.add(employee)
        print(f"{employee.name} has been added to {self.name}'s team.")

    def hold_meeting(self):
        print(f"{self.name} is holding a meeting with the team.")

class Engineer(Employee):
    def develop_feature(self):
        print(f"{self.name} is developing a new feature.")

class Salesperson(Employee):
    def make_sale(self):
        print(f"{self.name} is making a sale.")


class Animal:
    def breed(self):
        print("Breeding...")

    def eat(self):
        print("Eating...")

    def die(self):
        print("Dying...")

class Mammal(Animal):
    def walk(self):
        print("Walking...")

    def run(self):
        print("Running...")

class Bird(Animal):
    def fly(self):
        print("Flying...")

class Fish(Animal):
    def swim(self):
        print("Swimming...")



class LibraryItem:
    def __init__(self, title, item_id):
        self.title = title
        self.item_id = item_id
        self.checked_out = False

    def check_out(self):
        if not self.checked_out:
            self.checked_out = True
            print(f"{self.title} has been checked out.")
        else:
            print(f"{self.title} is already checked out.")

    def return_item(self):
        if self.checked_out:
            self.checked_out = False
            print(f"{self.title} has been returned.")
        else:
            print(f"{self.title} was not checked out.")

    def display_info(self):
        status = "Checked out" if self.checked_out else "Available"
        print(f"Title: {self.title}, ID: {self.item_id}, Status: {status}")

class Book(LibraryItem):
    def __init__(self, title, item_id, author, num_pages):
        super().__init__(title, item_id)
        self.author = author
        self.num_pages = num_pages

    def display_info(self):
        super().display_info()
        print(f"Author: {self.author}, Pages: {self.num_pages}")

class DVD(LibraryItem):
    def __init__(self, title, item_id, director, duration):
        super().__init__(title, item_id)
        self.director = director
        self.duration = duration

    def display_info(self):
        super().display_info()
        print(f"Director: {self.director}, Duration: {self.duration} minutes")

class Magazine(LibraryItem):
    def __init__(self, title, item_id, issue_number):
        super().__init__(title, item_id)
        self.issue_number = issue_number

    def display_info(self):
        super().display_info()
        print(f"Issue Number: {self.issue_number}")
