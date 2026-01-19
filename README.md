# School-Management-System

# XYZ School Management System

This is a **console-based School Management System** developed in Python.  
It allows users to **add students, enroll them in courses, and view all student information**.  
All data is stored in a text file (`student_info.txt`) so that it persists even after the program is closed.

---

## 📂 Project Structure

```
School-Management-System/
├── main.py         # Main console program
├── my_classes.py   # Contains Student and Course classes
├── my_methods.py   # All functions: save, show, input validation, roll uniqueness check
└── student_info.txt # Data file (created automatically when program runs)
```

---

## 📝 Use Cases

### 1. Add Student
- User inputs:
  - Name (non-empty string)
  - Roll Number (numeric, must be unique)
  - Password (non-empty string)
  - Number of courses to enroll (numeric)
  - Course names (non-empty strings)
- Program creates a `Student` object and enrolls the student in courses.
- Student data is saved in `student_info.txt`.

### 2. Show All Students
- Reads all data from `student_info.txt`.
- Prints all students line by line with their enrolled courses.

### 3. Exit
- Close the program gracefully.

---

## 🔐 Features
- **Encapsulation:** Student password is private and accessed only via a getter method.
- **File Handling:** All student information is saved in a text file to prevent data loss.
- **Input Validation:** 
  - Non-empty strings for name and password
  - Numeric only for roll and course count
  - Unique roll number enforced
- **Persistent Storage:** Data remains even after program exit.

---

## ⚙️ How to Run
1. Make sure Python 3 is installed.
2. Navigate to project folder.
3. Run the program:
```bash
python main.py
```
4. Follow the menu to add students, view students, or exit.

---

## 📄 Example student_info.txt Format

```
Imran,14,777,Math,Science
Rahim,15,888,English
```

- Name, Roll, Password, Courses (comma-separated)
- Courses are stored as strings in the file.

---

## ✅ Notes
- `student_info.txt` will be automatically created on first run.
- Ensure you **use unique roll numbers** for each student.
- The repository is public, ready for submission.
