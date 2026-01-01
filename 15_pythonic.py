
# 15. Pythonic Stuff

squares = [x**2 for x in range(5)]
print(squares)

for i, v in enumerate(["a", "b", "c"]):
    print(i, v)

names = ["A", "B"]
scores = [90, 80]
print(list(zip(names, scores)))

print(len(names))
