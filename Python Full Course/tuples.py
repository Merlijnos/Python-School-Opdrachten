student = ("Merlijn",15,"male")

print(student.count("Merlijn"))
print(student.index("male"))

for x in student:
    print(x)

if "Merlijn" in student:
    print("Merlijn is here!")