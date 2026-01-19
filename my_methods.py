#creating a file and adding student info
def save_student_info(s):
    with open('student_info.txt', 'a') as file:
        file.write(f"{s.name},{s.roll},{s.get_password()},{','.join(s.courses)}\n")

#for showing all student information
def show_all_student_info():
    try:
        with open('student_info.txt', 'r') as file:
            print("\n--- All Students ---")
            for line in file:
                print(line.strip()) #line by line print
            print("-------------------")
    except FileNotFoundError:
        print("\n--- No Students enrolled yet ---")

#<-----------------file handling ends here ------------------>


#user input validation function

#for valid user input
def get_nonempty_user_input(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        else:
            print("\n--Invalid input! Please try again.\n")


#for only numeric input for roll number
def get_numeric_user_input(prompt):
    while True:
        value = input(prompt).strip()
        if value.isdigit():
            return int (value)
        else:
            print("\n--Invalid input! Only numeric values are allowed.\n")


#for unique roll number
def get_unique_roll():
    while True:
        roll = get_numeric_user_input("Enter roll number (numeric only): ")
        if is_roll_unique(roll):
            return roll
        else:
            print(f"Roll number {roll} already exists! Enter a different roll number.")


#check roll unique or not
def is_roll_unique(roll):
    try:
        with open('student_info.txt', 'r') as file:
            for line in file:
                data = line.strip().split(',') #make each line as a list separated by comma
                if len(data) >= 2 and data[1] == str(roll): # if list has at least one value and second data match with roll
                    return False
    except FileNotFoundError:
        return True #if no file created return all roll is true
    return True





















