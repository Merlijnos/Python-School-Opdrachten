def collect_names_and_ages():
    names_and_ages = []
    while True:
        name = input("Enter a name: ")
        age = input("Enter an age: ")
        names_and_ages.append((name, age))
        continue_or_stop = input("Toets enter om door te gaan of stop om te printen: ")
        if continue_or_stop.lower() == "stop":
            break
    return names_and_ages

def print_names_and_ages(names_and_ages):
    for name, age in names_and_ages:
        print("Name:", name, "Age:", age)

names_and_ages = collect_names_and_ages()
print_names_and_ages(names_and_ages)