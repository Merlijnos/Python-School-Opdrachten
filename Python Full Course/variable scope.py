name = 'Merlijn' # global variable
 
def display_name():
    name = 'de Groot' # local variable
    print(name)

display_name()
print(name)