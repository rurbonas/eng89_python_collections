# Python Data Collection

- Lists
- Tuples
- Dictionaries
- Sets

# Lists (Arrays in other languages)

- Shopping lists - Multiple items, add, edit, delete, update
- CRUD - Create Read update and delete

#  Create a shopping list
```python
Syntax [] - name_of_list = ["items in list"]
```
```python
shoppingList = ["mango", "eggs", "tea", "bread", "apples", "tuna"]
print(shoppingList)
print(shoppingList.pop(3)) # Pop will remove and return the last item from the list unless an index is specified
print(shoppingList)

shoppingList = ["mango", "eggs", "tea", "bread", "apples", "tuna"]
print(shoppingList)
del shoppingList[0] # Del will remove the indexed item from the list
print(shoppingList)

shoppingList = ["mango", "eggs", "tea", "bread", "apples", "tuna"]
print(shoppingList)
shoppingList.remove("bread") # Del will remove the specified named item from the list
print(shoppingList)
```

##  Create a shopping tuple
```python
Syntax () - name_of_list = ("items in list")
```
Lists are MUTABLE tuples are IMMUTABLE (Unchangeable)
```python
shoppingTuple = ("mango", "eggs", "tea", "bread", "apples", "tuna")
# print(shoppingTuple.pop(3)) will return an error
```


### Dictionaries and Sets both are Data collections in Python

```python
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
```

### Sets are also Data collection
#### Syntax name = {"", "", ""}
#### Unlike dictionaries, sets are unoredered

```python
shopping_list = ["eggs", "tea", "milk"]
print(shopping_list)

# Sets don't display in order or repeating items, just what's in the set
car_parts = {"engine", "engine", "wheels", "gears"}
print(car_parts)
```