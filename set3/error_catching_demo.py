""" 
This script demonstrates how to catch errors in Python
you can modify it and make it throw different errors to see how it works
""" 

try:
    my_list = [1, 2, 3]
    print(my_list[5])  # <-- with throw an IndexError
    a = 1 / 0  # <-- with throw a ZeroDivisionError
except ZeroDivisionError as ze:
    print("I know your game", ze)
except IndexError as ie:
    print("I know your library card number!", ie)
except Exception as e:
    print("Generic error, this will catch everything", e)
finally:
    print("bye!")
