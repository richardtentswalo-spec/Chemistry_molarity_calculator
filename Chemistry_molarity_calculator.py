# CHEMISTRY MOLARITY CALCULATOR

def calculate_molarity():
    moles = float(input("Enter number of moles: "))
    volume = float(input("Enter volume(L): "))

    if volume == 0:
        print('Error: Volume cannot be zero')
    else:
        molarity = moles / volume
        print(f'Molarity is: {molarity:.2f}mol/L')

def calculate_dilution():
    c1 = float(input("Enter the initial concentration(c1): "))
    v1 = float(input('Enter the initial  volume(v1) : '))
    v2 = float(input('Enter final volume(v2) : '))

    if v2 == 0:
        print("Error: Final volume cannot by zero")
    else:
        c2 = (c1 * v1) / v2
        print(f"Final concentration(c2) is {c2:.2f}")


def display():
    print("\n----CHEMISTRY MOLARITY CALCULATOR----")
    print("1. Calculate Molarity")
    print("2. Calculate Dilution")
    print("3. Exit")

def main():
    choice = 0
    while choice != 3:
        display()

        choice = int(input("Choose an option: "))
        if choice == 1:
            calculate_molarity()
        elif choice == 2:
            calculate_dilution()
        elif choice == 3:
            print("Goodbye!")
        else:
            print("Invalid choice. Try again ")

main()
            
