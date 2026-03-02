variable = input("Variable: ")
snake = ""
for char in variable:
    if char.isupper():
        snake += "_" + char.lower()
    else:
        snake += char
print(snake)
