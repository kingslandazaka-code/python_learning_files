
# 10. Scope
#this shows how functions work
x = 10

def show():
    global x
    x += 5

show()
print(x)
