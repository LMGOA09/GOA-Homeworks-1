#7)
sent1 = input("Enter first sentence: ").lower()
sent2 = input("Enter second sentence: ").lower()

# extracting unique letters but ignoring punctuation:
set1 = {char for char in sent1 if char.isalpha()}
set2 = {char for char in sent2 if char.isalpha()}

print("Unique letters in 1st sentence:", len(set1))
print("Unique letters in 2nd sentence:", len(set2))
print("Letters in both sentences:", set1 & set2)
print("Letters only in 1st sentence:", set1 - set2)

#8)
A = {1, 2, 3, 4, 5, 6}
B = {4, 5, 6, 7, 8}
C = {6, 7, 8, 9, 10}

# (A ∪ B) ∩ C:
res1 = (A | B) & C
print("(A ∪ B) ∩ C:", res1)

# A − (B ∪ C):
res2 = A - (B | C)
print("A − (B ∪ C):", res2)

# (A ∩ B) ∪ (B ∩ C):
res3 = (A & B) | (B & C)
print("(A ∩ B) ∪ (B ∩ C):", res3)

# symmetric difference between A and B:
res4 = A ^ B
print("Symmetric difference (A ^ B):", res4)

# checking whether C is a subset of (A ∪ B):
is_subset = C.issubset(A | B)
print("Is C a subset of (A ∪ B)?:", is_subset)