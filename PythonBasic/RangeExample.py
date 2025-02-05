print(range(20))
print(list(range(20)))
print(list(range(4, 15)))
print((list(range(2, 20, 2))))

discussion="movies"
movies=["Troy", "Gladiator", "Ocean's 11"]
for i in range(len(movies)):
    if(discussion=="movies"):
        print("my fave: ",movies[i])
else:
    print("Nothing to be printed")


country="India"

countryInfo={'USA':200, 'India':250, 'UAE':150, 'Australia':100}
for placeholder in countryInfo:
    if placeholder==country:
        print(countryInfo[placeholder])
        break
else:
    print('country not found')