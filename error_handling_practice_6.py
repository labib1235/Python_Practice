try:
    raise NameError("Hey! It is a custom error message.")

except NameError as e:
    print(e)