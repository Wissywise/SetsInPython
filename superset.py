
"""
In Python, a set is a built-in data type used to store an unordered collection of unique items
Key Characteristics
Unique Elements: Sets automatically filter out duplicate values. If you add a duplicate, it is quietly ignored.
Unordered & Unindexed: Elements do not have a defined order, meaning they can appear differently every time you print
them. Because they lack order, you cannot access items using an index (e.g., my_set[0] will throw an error).
Highly Efficient: Under the hood, Python sets are implemented using hash tables. This makes membership testing
(checking if an item is in a set) almost instantaneous (O(1) time complexity), which is significantly faster
than checking a list.
Element Restrictions: While the set itself is mutable (you can add or remove items), the individual elements inside a
set must be immutable and hashable (like integers, floats, strings, or tuples). You cannot put a list or another
set inside a set
"""
#You can create a set by placing items inside curly braces {} or by using the set() constructor
# Creating a set with elements
fruits = {"apple", "banana", "cherry", "apple"}
print(fruits)
# Output: {'banana', 'apple', 'cherry'} (Notice "apple" only appears once and the order changed)

# WARNING: To create an EMPTY set, you MUST use set()
empty_set = set()      # Correct
not_a_set = {}         # Incorrect! This creates an empty dictionary

#Sets are highly valued in Python because they allow you to perform native mathematical operations
set_a = {1, 2, 3}
set_b = {3, 4, 5}

print(set_a | set_b)  # Union: {1, 2, 3, 4, 5}
print(set_a & set_b)  # Intersection: {3}
print(set_a - set_b)  # Difference: {1, 2}

fast_food_brands = frozenset({"McDonald's", "Burger King", "KFC", "Subway", "Wendy's"})

fast_food_brands.add("Domino's")

print(fast_food_brands)



