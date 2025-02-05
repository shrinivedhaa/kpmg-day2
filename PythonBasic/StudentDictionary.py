st1={"name": "nivi", "age": 22, "subjects": ["physics", "chemistry", "biology"]}
st2={"name": "mrunal", "age": 21, "subjects": ["maths", "chemistry", "english"]}
st3={"name": "prerana", "age": 22, "subjects": ["maths", "hindi", "history"]}
students=[]
students.append(st1)
students.append(st2)
students.append(st3)

print(students)

for i in students:
    print(i)

for i in students:
    print(i.get("name"))

marks={'nivi': 10, 'mrunal': 20, 'prerana': 30}
max=0
for i in marks:
    if marks[i]>max:
        max=marks[i]
        name=i

print("Name",name,"Marks", max)