
MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""
print(MENU)
choice = input(">>> ").upper()


def celsius_to_fahrenheit():
    global fahrenheit
    fahrenheit = celsius * 9.0 / 5 + 32


def farhenheit_to_celsius():
    celsuis = 5 / 9 * (fahrenheit - 32)


while choice != "Q":
    if choice == "C":
        celsius = float(input("Celsius: "))
        celsius_to_fahrenheit()
        print("Result: {:.2f} cF".format(fahrenheit))
    elif choice == "F":
        fahrenheit = float(input("Fahrenheit: "))
        farhenheit_to_celsius()
        print("Result:", celsius , "C")
        # TODO: Write this section to convert F to C and display the result
        # Hint: celsius = 5 / 9 * (fahrenheit - 32)
        # Remove the "pass" statement when you are done. It's a placeholder.
        pass
    else:
        print("Invalid option")
    print(MENU)
    choice = input(">>> ").upper()
print("Thank you.")