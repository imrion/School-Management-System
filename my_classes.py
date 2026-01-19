class Course:
    def __init__(self,name):
        self.name = name


class Student:
    def __init__(self,name,roll,password):
        self.name = name
        self.roll = roll
        self.courses = []
        self.__password = password  #this is private instance var


    def enroll_course(self,course):
        self.courses.append(course.name)  #add courses into instance list


    def get_password(self):     #private field accessing through a method
        return self.__password

