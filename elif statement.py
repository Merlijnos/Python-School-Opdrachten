print("Vul een variabele in")
a = int(input())
print("Vul een tweede variabele in")
b = int(input())
if a > b: 
    print("a is het grootste getal:" + str(a))
elif a < b:
    print("a is kleiner dan b:" + str(b))
else:
    print('a en b zijn evengroot')
max = a
min = b