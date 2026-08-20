# 4) Create a mixed list with all data types, then give the user the opportunity to delete an element from that list. 
# If they enter an existing element, remove it; if they enter a non-existing element, print "Invalid Choice" in the terminal.

my_list = [42, 3.14, "Hello", True, [1, 2, 3], {"key": "value"}]
print("Current list:", my_list)
element_to_remove = input("Enter the element you want to remove: ")
if element_to_remove in my_list:
    my_list.remove(element_to_remove)
    print("Updated list:", my_list)
else:
    print("Invalid Choice")