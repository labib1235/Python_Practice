try:
    with open("test.txt", "r") as my_file:
        content = my_file.read()
        print(content)
except:
    print("The file does not exist")
print("This is made by Labib")