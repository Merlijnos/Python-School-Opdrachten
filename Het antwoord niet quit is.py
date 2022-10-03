aantal = 0
for i in range(999):
    print('?')
    aantal += 1
    vraag = input()
    if vraag == 'quit':
        print(aantal)
        print(quit)