def hello(**names):
    # print('Hello '+ kwargs['first']+' '+ kwargs['last'])
    print('Hello',end=" ")
    for key,value in names.items():
        print(value,end=" ")

hello(title="Mr.",first="Merlijn",middle="de",last="Groot")