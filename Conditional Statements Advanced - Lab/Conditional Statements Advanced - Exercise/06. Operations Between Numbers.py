n1 = int(input())
n2 = int(input())
operator = input()
isEven = "odd"

if operator == "+":
    sabirane = n1 + n2
    if sabirane % 2 == 0:
        isEven = True
        if isEven:
            isEven = "even"
    print(f"{n1} {operator} {n2} = {sabirane} - {isEven}")
elif operator == "-":
    izvajdane = n1 - n2
    if izvajdane % 2 == 0:
        isEven = True
        if isEven:
            isEven = "even"
    print(f"{n1} {operator} {n2} = {izvajdane} - {isEven}")
elif operator == "*":
    umnojenie = n1 * n2
    if umnojenie % 2 == 0:
        isEven = True
        if isEven:
            isEven = "even"
    print(f"{n1} {operator} {n2} = {umnojenie} - {isEven}")
elif operator == "/":
    if n2 == 0:
        print(f"Cannot divide {n1} by zero")
    else:
        delenie = n1 / n2
        print(f"{n1} {operator} {n2} = {delenie:.2f}")
elif operator == "%":
    if n2 == 0:
        print(f"Cannot divide {n1} by zero")
    else:
        modulnoDelenie = n1 % n2
        print(f"{n1} {operator} {n2} = {modulnoDelenie}")

