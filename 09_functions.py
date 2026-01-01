
# 9. Functions

def greet(name="User"):
    return f"Hello, {name}"

print(greet())
print(greet("Kingsland"))

def add(*args):
    return sum(args)

print(add(1, 2, 3))
