#string=input()
try:
    num=int(input())
    #print(string+num)
    print(10+num)
except TypeError as te:
    print(te)
    print("Type Error")
except ValueError as ve:
    print(ve)