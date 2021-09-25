try:
    with open("test.txt", "r") as my_file:
        content = my_file.read()
        print(content)

except FileNotFoundError:
    print("The file does not exist")

finally:
    print("To be or not to be that is a question.")