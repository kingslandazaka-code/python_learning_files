
# 12. Error Handling

# TRY–EXCEPT–FINALLY block
# Used to handle errors without crashing the program

try:
    # Attempt to convert a string to an integer
    # "abc" is not a valid number, so this will cause an error
    num = int("abc")

except ValueError:
    # This block runs ONLY if a ValueError occurs in the try block
    # ValueError happens when the type is correct but the value is wrong
    print("Conversion failed")

finally:
    # This block ALWAYS runs
    # Whether an error occurred or not
    # Used for cleanup actions (closing files, releasing resources, etc.)
    print("Done")
