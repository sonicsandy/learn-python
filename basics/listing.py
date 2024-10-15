import math

def test_func():
    """
    This is a test function, returns void
    """
    for i in range(1, 10, 2):
        print(i)
        i = i + 1
        print(i)

# List
students = ["bob", "henry", "john", "micky", "steve"]

# For loop
for student in students:
    print(student)

print("\n")

# Exceptions
try:
    z=1/0
except ZeroDivisionError as zde:
    print("Exception: ", zde)
except Exception as e:
    print("Exception: ", e)

# Function call
test_func()

print("\n")

# Math lib/module
print(math.sqrt(16))

print(dir(math))