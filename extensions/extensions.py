file = input("Attach your file: ")
list = [".png", ".jpeg", ".jpg"]
list2 = [".pdf"]
list3 = [".txt"]
if file in list:
    print("This file is an image")
elif file in list2:
    print("This is a PDF")
elif file in list3:
    print("This file is a text")
else:
    print("")