# while 1==1:
#     print("I'm stuck i n a loop!")

name = ""
# name = None

# while not name:
while len(name) == 0:
    name = input('Enter your name: ')

    print("Hello "+name)