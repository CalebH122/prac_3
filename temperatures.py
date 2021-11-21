MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""


def main():
    print(MENU)

    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            fahrenheit = fahrenheit_cal()
            print("Result: {:.2f} F".format(fahrenheit))
        elif choice == "F":
            celsius = celsius_cal()
            print("Result: {} C".format(celsius))
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")


def celsius_cal():
    fahrenheit = float(input("Fahrenheit: "))
    celsius = 5 / 9 * (fahrenheit - 32)
    return celsius


def fahrenheit_cal():
    celsius = float(input("Celsius: "))
    fahrenheit = celsius * 9.0 / 5 + 32
    return fahrenheit


main()
