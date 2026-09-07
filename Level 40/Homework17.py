#1)
# {"abc"} creates a set with a single string element: {'abc'} (length 1);
# set("abc") passes the string to the set() constructor, which iterates over each character, returning: {'a', 'b', 'c'} (length 3).

# demo:
single_element_set = {"abc"}
character_set = set("abc")

print(single_element_set)
print(character_set)

#2)
# b = {} belongs to the dict (dictionary) data type. Python's dictionary syntax pre-dates set syntax, so {} was reserved for empty 
# dictionaries;
# Because {} creates an empty dictionary, set() must be used to create an empty set.

# demo:
b = {}
print(type(b))

empty_set = set()
print(type(empty_set))

#3)
# remove(element) raises a KeyError if the element is not found in the set;
# discard(element) removes the element if present, but does nothing (no error) if the element is not found.

# demo:
s = {1, 2, 3}

s.discard(99)
print("After discard:", s)

#4)
words = ["apple", "banana", "apple", "orange", "banana", "kiwi"]

words_set = set(words)

print("Original list length:", len(words))
print("Set length:", len(words_set))
print("Unique set:", words_set)

# Explanation:
# The lengths differ because lists allow duplicate elements ("apple" and "banana" appear twice),
# whereas sets automatically remove duplicate entries upon creation.