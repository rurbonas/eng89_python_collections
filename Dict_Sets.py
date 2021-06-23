students_1 = {
    "name": "James",
    "stream": "DevOps",
    "completed_lessons": 4,
    "lessons_learned": ["data types", "git and github", "operators"]
}

print(students_1)
print(type(students_1))
print(students_1["stream"])
print(students_1["lessons_learned"][-2]) #return second last lesson

print(students_1.keys()) # this method will return only the keys in the dictionary

print(students_1.values()) # this method will return only the values (without keys)

# Sets are also Data collection
# Syntax name = {"", "", ""}
# Unlike dictionaries, sets are unoredered

shopping_list = ["eggs", "tea", "milk"]
print(shopping_list)

# Sets don't display in order or repeating items, just what's in the set
car_parts = {"engine", "engine", "wheels", "gears"}
print(car_parts)

