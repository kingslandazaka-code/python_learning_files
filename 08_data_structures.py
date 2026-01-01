
# 8. Data Structures

# LIST
# A list is an ordered, changeable (mutable) collection of items
numbers = [1, 2, 3]

# append() adds a new item to the end of the list
numbers.append(4)

# The list is now modified
print(numbers)   # Output: [1, 2, 3, 4]


# TUPLE
# A tuple is an ordered but unchangeable (immutable) collection
coords = (10, 20)

# You cannot modify a tuple like a list
# coords[0] = 5  ❌ This would cause an error


# SET
# A set stores unique values only (no duplicates)
unique = {1, 2, 3, 3}

# Duplicate values are automatically removed
print(unique)   # Output: {1, 2, 3}


# DICTIONARY
# A dictionary stores data in key : value pairs
student = {
    "name": "Alex",
    "age": 20
}

# get() safely retrieves the value for a key
# If the key does not exist, it returns None instead of crashing
print(student.get("name"))   # Output: Alex
