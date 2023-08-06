operations = {
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y,
    "*": lambda x, y: x * y,
    "/": lambda x, y: x / y,
}

def calculate(expr):
    numxChars = ""
    operation = None
    numyChars = ""
    for char in expr:
        if char.isdigit():
            if operation is None:
                numxChars += char
            else:
                numyChars += char
        elif char in operations:
            operation = char
        elif char.isspace:
            pass
        else:
            raise Exception("invalid charecter: " + char)
    return operations[operation](int(numxChars), int(numyChars))
    
print (calculate(input("Input? ")))