expression = input("Equation: ")
x, y, z = expression.split(" ")
x = float(x)
z = float(z)

if y == "+":
    answer = x + z
    print(answer)
elif y == "-":
    answer = x - z
    print(answer)
elif y == "*":
    answer = x * z
    print(answer)
elif y == "/" and z == 0:
    print("Error") 
elif y == "/":
    answer = x / z
    print(answer)
else:
    print("I am not able to calculate that for u! ")