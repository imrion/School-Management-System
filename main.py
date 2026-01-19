from my_classes import Student,Course
from my_methods import *

def main():
    while True:
        print("\n===== XYZ School Management System ====")
        print("1. Add Student")
        print("2. Show All Students")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            name = get_nonempty_user_input("Enter your name: ")
            roll = get_unique_roll()
            password = get_nonempty_user_input("Enter your password: ")

            #-----Creating Student Object-----
            student = Student(name,roll,password)

            #-----Number of course validation
            course_number = int(get_numeric_user_input("How many courses to enroll? (numeric only): "))
            for i in range(course_number):
                course_name = get_nonempty_user_input(f"Enter name of course {i+1}: ")

                #-----creating course object-----
                course = Course(course_name)
                student.enroll_course(course)

            save_student_info(student)
            print("Student enrolled successfully!")

        elif choice == "2":
            show_all_student_info()

        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice! Try again.")

if __name__ == "__main__":
    main()