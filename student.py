class StudentDatabase:
    student_list = []
    def add_student(self, student):
        self.student_list.append(student)

class Student:
    
    def __init__(self, student_id, name, department, is_enrolled):
        self.__student_id = student_id
        self.__name = name
        self.__department = department
        self.__is_enrolled = is_enrolled
    
    def  enroll_student(self):
        if self.__is_enrolled:
            print(f"{self.__name} has already enrolled!")
        else:
            self.__is_enrolled = True
            print(f"{self.__name}'s enrollment successful!")

    def drop_student(self):
        if self.__is_enrolled:
            self.__is_enrolled = False
            print(f"{self.__name} has been dropped.")
        else:
            print(f"{self.__name} has already been dropped.")
    
    def view_student_info(self):
        print(f"ID: {self.__student_id}, Name: {self.__name}, Department: {self.__department}, Enrolled: {self.__is_enrolled}")
        return self.__student_id

data_base = StudentDatabase()
s1 = Student("S101", "Tayyib Imam Asif", "CSE", False)
s2 = Student("S102", "Mirza Tafhim Osman", "CSE", False)
s3 = Student("S103", "Nazib Rayhan Mahi", "CSE", False)
data_base.add_student(s1)
data_base.add_student(s2)
data_base.add_student(s3)
# s.enroll_student()
# s.view_student_info()

#flag =  True
while True:
    print("--- Student Management Menu ---")
    print("1.View All Students")
    print("2.Enroll Student")
    print("3.Drop Student")
    print("4.Exit")

    option = int(input("Enter Your Choice (1-4): "))
    if option == 1:
        for student in data_base.student_list:
            student.view_student_info()
    
    elif option == 2:
        given_id = input("Enter Student ID: ")
        is_found = False
        for student in data_base.student_list:
            if student._Student__student_id == given_id:
                student.enroll_student()
                is_found = True
                break
        if not is_found:
            print(f"{given_id} ID Not Found!")
    
    elif option == 3:
        given_id = input("Enter Student ID: ")
        is_found = False
        for student in data_base.student_list:
            if student._Student__student_id == given_id and not student._Student__is_enrolled:
                print("Student hasn't enrolled yet!")
                is_found = True
                break
                
            elif student._Student__student_id == given_id:
                student.drop_student()
                is_found = True
                break

        if not is_found:
            print(f"{given_id} ID Not Found!")
    elif option == 4:
        print("Exiting...")
        break
    else:
        print("Invalid Input!")

# print(dir(s))
# _Student__student_id


