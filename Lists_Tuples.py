#  Create a shopping list
# Syntax [] - name_of_list = ["items in list"]
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

#  Create a shopping tuple
# Syntax () - name_of_list = ("items in list")
# Lists are MUTABLE tuples are IMMUTABLE (Unchangeable)

shoppingTuple = ("mango", "eggs", "tea", "bread", "apples", "tuna")
# print(shoppingTuple.pop(3)) will return an error