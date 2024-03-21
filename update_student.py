# Define a dictionary to store student grades
student_grades = {}

# Function to add grades for a student
def add_grades(student_id, grades):
    student_grades[student_id] = grades

# Function to retrieve grades for a student
def get_grades(student_id):
    return student_grades.get(student_id, "No grades found for this student.")

# Example usage
add_grades("John", {"Math": 85, "Science": 90, "History": 75})
add_grades("Alice", {"Math": 90, "Science": 95, "History": 80})

# Retrieve grades for a student
print("Grades for John:", get_grades("John"))
print("Grades for Alice:", get_grades("Alice"))

# Attempt to retrieve grades for a student not in the dictionary
print("Grades for Bob:", get_grades("Bob"))
