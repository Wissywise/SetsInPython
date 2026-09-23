college_name = "Texas Tech University"


print(f" Welcome to {college_name} AI Course Prerequisites Checker!\n")


texas_tech_ai_prerequisites = {
    "Math", "Programming", "Data Structures", "Machine Learning",
    "Statistics", "Linear Algebra", "Artificial Intelligence"
}


student_courses = set(input("Enter your completed courses (comma separated): ").split(","))


student_courses = {course.strip() for course in student_courses}


if texas_tech_ai_prerequisites.issubset(student_courses):
    print(f"\n Congratulations! You meet the prerequisites for the Artificial Intelligence "f" course at {college_name}!")
else:
    print(f"\n You do not meet the prerequisites for the Artificial Intelligence course at {college_name}.")
    print("You need to complete these courses first:")

    for course in texas_tech_ai_prerequisites - student_courses:
        print("-", course)
