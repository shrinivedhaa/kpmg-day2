import TempConvertor

celsius = int(input("Enter the temperature in celsius: "))
toFar = TempConvertor.CelToFar(celsius)
print("The temperature in fahrenheit is ",toFar)

fahrenheit = int(input("Enter the temperature in fahrenheit: "))
toCel = TempConvertor.FarToCel(fahrenheit)
print("The temperature in celsius is ",toCel)
