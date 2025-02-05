class InvalidCardLength(Exception):
    def __init__(self, cardno, message="Card number length must be 12 or 16"):
        self.cardno=cardno
        self.message=message
        super().__init__(self.message)

def validate_card(cardno):
    if len(cardno)!=12 and len(cardno)!=16:
        raise InvalidCardLength(cardno)
    else:
        print("Number is valid")

try:
    cardnumber=input("Enter your card number: ")
    validate_card(cardnumber)
except InvalidCardLength as e:
    print(f"InvalidCardLength: {e}")
except ValueError:
    print("Error: Please enter a valid integer.")
finally:
    print("Card number validation complete")