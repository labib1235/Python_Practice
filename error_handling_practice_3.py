try:
    my_file = open("test.txt")
    content = my_file.read()
    i = int(content.strip())

except IOError as e:
    errno, strerror = e.args
    print("I/O error({0}): {1}".format(errno, strerror))

except ValueError:
    print("No valid integer in line.")

except:
    print("Unexpected error.")