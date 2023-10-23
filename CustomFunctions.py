def kennedy():
    print("My Name is Kennedy ")


kennedy()


# a function cannot work without controller

def adding():
    num = int(input("Enter First Number"))
    num2 = int(input("Enter Second Number"))
    print(f"sum of {num} and {num2} is {num + num2}")

adding()

def toshiba_class(Fname, Lname, Class, Age):
    print(f"Student First name: {Fname} Last Name: {Lname}, "
          f"attending {Class}, he/she is {Age} years old")
toshiba_class("Kennedy", "Kimani", "emobilis", "27")
