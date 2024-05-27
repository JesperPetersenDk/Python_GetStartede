

def helloName():
    name = print("Hej", input("What is your name?"))
    return name

def addNumber(numberInput):
    ex = sum(numberInput)
    print(ex)

commands = input("Brug disse commands: hello, number")

if(commands.lower() == "number"):
    expNumber = [22.2, 55.2, 66.2, 88.2, 103.3, 140.51]
    addNumber(expNumber)
elif(commands.lower() == "hello"):
    helloName()
