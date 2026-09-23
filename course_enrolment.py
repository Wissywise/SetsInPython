#Python Set Enrollment Analysis (Fully Commented)

# Create a set of students enrolled in the Python for Beginners course.
# Sets automatically remove duplicates and do not keep order.

beginners = {"Emma", "Liam", "Olivia", "Noah"}

# Create a set of students enrolled in the Python Projects course.

projects = {"Liam", "Olivia", "Sophia", "Ava"}


# -------------------------------
# Students enrolled in BOTH courses
# -------------------------------

# .intersection() returns only the elements that appear in BOTH sets.

both = beginners.intersection(projects)

# Print the result so we can see which students are in both classes.

print("Enrolled in both courses:", both)


# -------------------------------
# Students ONLY in the Beginners course
# -------------------------------

# .difference() returns items that are in the first set but NOT in the second.

only_beginners = beginners.difference(projects)

# Print the students who are only taking the beginner course.

print("Only in Beginners course:", only_beginners)


# -------------------------------
# Students ONLY in the Projects course
# -------------------------------

# Same idea as above, but reversed.

only_projects = projects.difference(beginners)

# Print the students who are only taking the project course.

print("Only in Projects course:", only_projects)


# -------------------------------
# Total unique students across BOTH courses
# -------------------------------

# .union() combines both sets and removes duplicates automatically.

total_unique = beginners.union(projects)

# Print the full set of unique students.

print("Total unique students:", total_unique)

"""
 Expected Output

Enrolled in both courses: {'Olivia', 'Liam'}
Only in Beginners course: {'Noah', 'Emma'}
Only in Projects course: {'Sophia', 'Ava'}
Total unique students: {'Emma', 'Liam', 'Ava', 'Olivia', 'Sophia', 'Noah'}
"""