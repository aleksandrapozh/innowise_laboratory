# Initialize an empty list to store student data
students = []
choice = 0

def add_new_student():
    """Function for adding a new student to the system"""
    student_name = input('Enter student name: ')

    # Check if a student with this name exists
    for student in students:
        if student['name'].lower() == student_name.lower():
            print(f'Student {student_name} already exist!')
            return # Exit the function if the student already exists

    # Create a new student in the form of a dictionary
    new_student = {
        'name': student_name,
        'grades': []
    }

    students.append(new_student)


def add_grades_for_student():
    """Function for adding grades to an existing student"""
    student_name = input('Enter student name: ')
    for student in students:
        if student['name'].lower() == student_name.lower():
            grade_or_done = ''
            while True:
                grade_or_done = input("Enter a grade (or 'done' to finish): ")
                if grade_or_done.lower() == 'done':
                    break

                try:
                    grade = int(grade_or_done)
                    if 0 <= grade <= 100 :
                        student['grades'].append(grade)
                    else:
                        print("Grade must be between 0 and 100")
                except ValueError:
                    print('Invalid input. Please enter a number')

            return

    # If the student is not found
    print('This student is not here yet')

def show_report():
    """Function for generating a full report on all students"""
    print('--- Student Report ---')
    dict_grades = []
    for student in students:
        try:
            average_grade = sum(student['grades'])/len(student['grades'])
            dict_grades.append(average_grade)
            print(f"{student['name']}'s average grade is {average_grade:.1f}")
        except ZeroDivisionError:
            # Handle the case when a student has no grades
            average_grade = 'N/A'
            print(f"{student['name']}'s average grade is {average_grade}")

    if not students:
        print('There are no students here yet')
    elif not dict_grades:
        print('No students have grades yet')
    else:
        print('--------------------------')
        max_avg = max(dict_grades)
        min_avg = min(dict_grades)
        overall_avg = sum(dict_grades) / len(dict_grades)

        print(f'Max Average: {max_avg:.1f}')
        print(f'Min Average: {min_avg:.1f}')
        print(f'Overall Average: {overall_avg:.1f}')

def find_top_performer():
    """Function for finding the student with the highest grade point average"""
    print('--- Top Performer ---')

    if not students:
        print('No students found.')
        return

    # Create a list of students who have grades
    students_with_grades = [student for student in students if student['grades']]

    if not students_with_grades:
        print('No students with grades found.')
        return

    # Find the student with the highest average grade
    top_student = max(students_with_grades, key=lambda student: sum(student['grades']) / len(student['grades']))

    # Calculate the average grade of the best student
    average_grade = sum(top_student['grades']) / len(top_student['grades'])

    print(f"Top performer is {top_student['name']} with average grade {average_grade:.1f}")


while True:
    print('--- Student Grade Analyzer ---')
    print('1. Add a new student\n'
        '2. Add grades for a student\n'
        '3. Generate a full report\n'
        '4. Find the top student\n'
        '5. Exit')

    choice = input('Enter your choice: ')

    match choice:
        case '1':
            add_new_student()
        case '2':
            add_grades_for_student()
        case '3':
            show_report()
        case '4':
            find_top_performer()
        case "5":
            print('Exiting program.')
            break
        case _:
            # Handling invalid selections
            print("Invalid choice")



