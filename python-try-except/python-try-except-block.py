try:
    print(x)
except:
    print("An exception occurred")
finally:
    print("we are in finally block")


try:
    print(x)
except NameError:
    print("Variable x is not defined")
except:
    print("Something else went wrong")
finally:
    print("we are in finally block")

# What's the purpose of the else block.
try:
    print("Hello")
except:
    print("Something went wrong")
else:
    print("Nothing went wrong")

try:
    print("Hello")
except:
    print("Something went wrong")
print("Nothing went wrong")

