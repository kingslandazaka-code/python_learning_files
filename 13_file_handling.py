
# 13. File Handling


with open("sample.txt", "w") as f:
    f.write("Hello File")

# to read a .txt file
with open("sample.txt", "r") as f:
    print(f.read())
