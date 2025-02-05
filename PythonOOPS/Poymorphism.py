class Tomato():
    def type(self):
        print("vegetable")
    def color(self):
        print("red")

class Apple():
    def type(self):
        print("fruit")
    def color(self):
        print("red")

def func(obj):
    obj.type()
    obj.color()

obj_tomato=Tomato()
obj_apple=Apple()
func(obj_tomato)
func(obj_apple)

print("*********")

for fruitsAndVeggie in (obj_apple, obj_tomato):
    fruitsAndVeggie.type()
    fruitsAndVeggie.color()

print("*****Country Example*****")
class India():
    def capital(self):
        print("New Delhi")
    def language(self):
        print("hindi")

