#encapsulation and class object creation
class Book:
    def __init__(self, title, quantity, author, price):
        self.title=title
        self.quantity=quantity
        self.author=author
        self.price=price
        self.__publisher="Global Publisher"

    def set_sublisher(self, publisher):
        self.__publisher=publisher

    def get_publisher(self):
        return self.__publisher
    
    def __repr__(self):
        return f"Book: {self.title}, Quantity:{self.quantity}, Author:{self.author}, Price:{self.price}, Publisher:{self.get_publisher()}"
    
book1=Book("Tell Me Your Dreams",5,"Sidney Sheldon", 100)
book2=Book("The Firm",5,"John Grisham",120)
book3=Book("The Partner",6,"John Grisham", 234)

print(book1)
print(book2)
print(book3)

print(book3.get_publisher())