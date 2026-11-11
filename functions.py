def addition():
    a = 10.9
    b = 45.0
    print(a + b)

addition()

def addition_input():
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))
    print(a + b)

addition_input()

def user_info(name, age, city):
    '''This function prints name, age and city
    from an argument provided to the function.'''
    print("{} is {} years old, from {}".format(name, age, city))

user_info("Janet", 58, "Oklahoma City")

def user_info_keyword(name, age=0, city="Tucson"):
    '''This function prints name, age and city
    from an argument provided to the function.'''
    print("{} is {} years old, from {}".format(name, age, city))

user_info_keyword("Micah")
user_info_keyword(age=56, name="Kadeem")

def add(*args):
    print(sum(args))

add(2, 3, 4)
add(2, 4, 6, 8, 184)

def application(**kwargs):
    print(kwargs)

application(name="Jess", email="mail@mail.com")
application(name="Susan", surname="Johnson", age=42)

def application_combine(fname, lname, email, company,
                *args, **kwargs):
    print("{} {} works at {}. Her email is {}. Her salary is {}. Her hire date is {}."
          .format(fname, lname, company, email, args[0], kwargs["hire_date"]))

application_combine("Jess", "Ingrass", "mail@mail.com",
                    "TeachCode.org", 75000, hire_date="September 2010")
