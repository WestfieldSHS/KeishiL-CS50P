def main():
    file = input("Attach your file: ")
    file = file.lower()
    file = file.replace(" ","")

    if file .endswith(".png"):
        print("Image/png")
    elif file .endswith(".jpg") or file .endswith(".jpeg"):
        print("Image/jpg")
    elif file . endswith(".pdf"):
        print("application/pdf")
    elif file .endswith(".gif"):
        print("Image/gif")
    elif file .endswith(".txt"):
        print("text/text")
    elif file .endswith(".pdf"):
        print("document/pdf")
    elif file .endswith(".zip"):
        print("file/zip")
    else:
        print("application/octet-stream")

main()