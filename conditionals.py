name = input("What's your name? ")
if name == "Jessica":
    print("Hello, nice to see you {}!".format(name))
elif name == "Danielle":
    print("Hello, you are a great person!")
# elif name != "Mariah":
#     print("You're not Mariah!")
elif name == "Kingston":
    print("Hi, {},  let's have lunch soon!".format(name))
else:
    print("Have a nice day!")

def check_if():
    name = input("What is your name?")
    if name == "Jess":
        print("Hi, Jess")
    print("Thanks for entering your name, " + name)

check_if()

def check_if_elif():
    name = input("What is your name?")
    if name == "Jess":
        print("Hi, Jess")
    elif name == "Bob":
        print("Hi, Bob")
    print("Thanks for entering your name, " + name)

check_if_elif()

def check_if_elif_else():
    name = input("What is your name?")
    if name == "Jess":
        print("Hi, Jess")
    elif name == "Bob":
        print("Hi, Bob")
    else:
        print("hi hi hi hi hi ")
    print("Thanks for entering your name, " + name)

check_if_elif_else()