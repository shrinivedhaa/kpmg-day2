class InvalidAgeError(Exception):
    def __init__(self, age, message="Age must be between 18 and 60."):
        self.age=age
        self.message=message
        super().__init__(self.message)

def validate_age(age):
    if age<18 or age>60:
        raise InvalidAgeError(age)
    else:
        print("Age is valid")

try:
    user_age=int(input("Enter your age: "))
    validate_age(user_age)
except InvalidAgeError as e:
    print(f"InvalidAgeError: {e}")
except ValueError:
    print("Error: Please enter a valid integer.")
finally:
    print("Age validation complete")