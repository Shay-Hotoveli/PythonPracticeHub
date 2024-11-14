import os

file_name = "calculation.log"

stored_last_calculations = []

def storing_calculations(par1, par2, action, result):
    stored_last_calculations.append(f"{par1} {action} {par2}: {result}")
    with open(file_name, "a")as file:
        file.write(f"{stored_last_calculations[-1]}\n")

#operator functions
def addition(par1, par2):
    result = par1 + par2
    storing_calculations(par1, par2, "+", result)
    return result
def subtraction(par1,par2):
    result = par1 - par2
    storing_calculations(par1, par2, "-", result)
    return result
def multiplication(par1,par2):
    result = par1 * par2
    storing_calculations(par1, par2, "*", result)
    return result
def division(par1,par2):
    if par2 != 0:
        result = par1 / par2
        storing_calculations(par1, par2, "/", result)
        return result
    else:
        print(f"Division by {par2} is not allowed")
def modulus(par1,par2):
    if par2 != 0:
        result = par1 % par2
        storing_calculations(par1, par2, "%", result)
        return result
    else:
        print(f"Modulus by {par2} is not allowed")
def exponentiation(par1, par2):
    result = par1 ** par2
    storing_calculations(par1, par2, "**", result)
    return result
def floor_division(par1, par2):
    if par2 != 0:
        result = par1 // par2
        storing_calculations(par1, par2, "//", result)
        return result
    else:
        print(f"Floor division by {par2} is not allowed")


#calculate func
def calculate(inp1, inp2, action):
    match action:
        case "+":
            return addition(inp1,inp2)
        case "-":
            return subtraction(inp1,inp2)
        case "*":
            return multiplication(inp1,inp2)
        case "/":
            return division(inp1,inp2)
        case "%":
            return modulus(inp1,inp2)
        case "**":
            return exponentiation(inp1,inp2)
        case "//":
            return floor_division(inp1, inp2)
        case _:
            print(f"'{action}' is not a valid operation, Try again.")
            return None
#checking validation of number
def is_valid_number(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

#getting user inputs
def arg_inputs():
    while True:
        number1 = input("First number: ")
        action_sign = input("Action: (,+ -, *, /, %, **, //): ")
        number2 = input("Second number: ")
        if not is_valid_number(number1) or not is_valid_number(number2):
            print(f"Number one: '{number1}' or Number two: '{number2}' is not a valid input. Try again ")
            continue
        inp1, inp2 = float(number1), float(number2)
        if action_sign in ('+', '-', '*', '/', '%', '**', '//'):
            result = calculate(inp1, inp2, action_sign)
            if result is not None:
                print("Result:", result)
                break
        else:
            print(f"'{action_sign}': Is not valid action. Try one of these (,+ -, *, /, %, **, //)")

#print last stored calculations from calculations.txt
def view_calculations():
    if not os.path.exists(file_name):
        print("No calculations have been logged yet.")
    else:
        print("\nStored Calculations:")
        with open(file_name, "r") as file:
            for line in file:
                print(line.strip())

#clearing log file
def clear_log():
    stored_last_calculations.clear()
    if os.path.exists(file_name):
        try:
            with open(file_name, "w"):
                pass
            print("Log cleared.")
        except Exception as e:
            print(f"An error occured while clearing the log:\n {e}")
    else:
        print("No log file found to clear.")


def menu():
    while True:
        print("\nMain Menu")
        print("1: Perform a Calculation")
        print("2: View Last Calculations")
        print("3: Clear Calculations Log")
        print("4: Quit")
        choice = input("Select an option (1-4): ")


        if choice == "1":
            arg_inputs()
        elif choice == "2":
            view_calculations()
        elif choice == "3":
            clear_log()
        elif choice == "4":
            print("Exiting the calculator. Goodbye!")
            break
        else:
            print("Invalid option. Please select a number between 1 and 4.")


menu()





