def function(fname):
    end = ""
    for x in range(1, fname + 1):
        end += f"Hello from function town {x}\n"
    return end    
userInput = int(input("Hoeveel?"))
print(function(userInput))