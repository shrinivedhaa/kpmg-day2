def divide_numbers():
    try:
        num1=float(input("Enter the numerator: "))
        num2=float(input("Enter the denominator: "))
        result=num1/num2
        print(f"Result: {result:.2f}")
    except ValueError:
        print("Error: Invalid input. please enter numeric values")
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    else:
        print("Division performed successfully")
    finally:
        print("Exiting division function.\n")

def read_file(filename):
    try:
        with open(filename,'r') as file:
            content=file.read()
            print("File content:\n", content)
    except FileNotFoundError:
        print("Error: File not found.")
    except PermissionError:
        print("Error: Insufficient permissions to read the file")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        print("File operation complete.\n")


def process_list_element():
    try:
        my_list=[10,20,30]
        index=int(input("Enter index (0-2) to access the list element: "))
        print(f"Element at index {index}: {my_list[index]}")
    except IndexError:
        print("Error: Index out of range.")
    except ValueError:
        print("Error: Please enter a valid integer.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        print("List  processing complete.\n")

#Main execution
'''if _name_=="_main_":'''
divide_numbers()
read_file("demofile.txt")
process_list_element()