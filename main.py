'''- Xây dựng 3 lớp Person, Student và Professor như bảng thiết kế ở trên
- Nhập dữ liệu từ bàn phím cho danh sách 10 Person
- Nhập dữ liệu (có thể tạo trong chương trình hoặc từ bàn phím) cho danh sách 10 Student
- Nhập dữ liệu cho danh sách 10 Professor
- In kết quả 3 danh sách trên ra màn hình
- Sắp xếp danh sách Person giảm dần theo Name; sắp xếp danh sách Student giảm dần theo
Average Mark; và sắp xếp danh sách Professor tăng dần theo Salary
- Lưu tuần tự 3 danh sách này vào 3 tập tin khác nhau (sử dụng pickle)
- Đọc các tập tin này và in kết quả ra màn hình.
'''

import pickle


class Person:
    def __init__(self, name=None, phoneNumber=None, email=None):
        self.name = name
        self.phoneNumber = phoneNumber
        self.email = email

    def outputInfo(self):
        return f"Name: {self.name}, Phone: {self.phoneNumber}, Email: {self.email}"

    def checkClass(self):
        return "Person"


class Student(Person):
    def __init__(self, name=None, phoneNumber=None, email=None, studentNumber=None, averageMark=None):
        super().__init__(name, phoneNumber, email)
        self.studentNumber = studentNumber
        self.averageMark = averageMark

    def outputInfo(self):
        return f"Name: {self.name}, Phone: {self.phoneNumber}, Email: {self.email}, Student Number: {self.studentNumber}, Average Mark: {self.averageMark}"

    def checkClass(self):
        return "Student"


class Professor(Person):
    def __init__(self, name=None, phoneNumber=None, email=None, salary=None):
        super().__init__(name, phoneNumber, email)
        self.salary = salary

    def outputInfo(self):
        return f"Name: {self.name}, Phone: {self.phoneNumber}, Email: {self.email}, Salary: {self.salary}"

    def checkClass(self):
        return "Professor"


''' Function: Input list include 10 object
    Input: List hold object
    Output: List hold object after inputting
'''


def inputClassList(objectList):
    for i in range(0, 2):
        print(i + 1)
        # Input information of person
        inputName = input("Enter the name: ")
        inputPhoneNumber = input("Enter the phone number: ")
        inputEmail = input("Enter the email address: ")
        # assign value to object
        objectList[i].name = inputName
        objectList[i].phoneNumber = inputPhoneNumber
        objectList[i].email = inputEmail
        if objectList[i].checkClass() == "Person":
            continue
        elif objectList[i].checkClass() == "Student":
            # Input information of student
            inputStudentNumber = input("Enter the student number: ")
            inputAverageMark = input("Enter the average mark: ")
            # assign value to object
            objectList[i].studentNumber = inputStudentNumber
            objectList[i].averageMark = inputAverageMark
        elif objectList[i].checkClass() == "Professor":
            # input information of professor
            inputSalary = input("Enter the salary: ")
            # assign value to object
            objectList[i].salary = inputSalary
    return objectList


def main():
    # Class Person
    # Initialize list include object of class Person
    personList = [Person() for i in range(0, 2)]
    inputClassList(personList)
    # Sort list of people descending with name
    personList.sort(key=lambda x: x.name, reverse=True)
    # Save file with Pickle
    file1 = open("D:\Person.txt", "wb")
    pickle.dump(personList, file1)
    file1.close()
    # Read file and print screen
    file1 = open("D:\Person.txt", "rb")
    personObjectList=pickle.load(file1)
    print("Person list:")
    for i in range(0, 2):
        print(personObjectList[i].outputInfo())  # Because pickload(file1) is list include object of class Person
    file1.close()

    # Class Student
    # Initialize list include object of class Student
    studentList = [Student() for i in range(0, 2)]
    inputClassList(studentList)
    # Sort list of student descending with average mark
    studentList.sort(key = lambda x: x.averageMark, reverse=True)
    # Save file with Pickle
    file2 = open("D:\Student.txt", "wb")
    pickle.dump(studentList, file2)
    file2.close()
    # Read file and print screen
    file2=open("D:\Student.txt", "rb")
    studentObjectList = pickle.load(file2)
    print("Student list:")
    for i in range(0, 2):
        print(studentObjectList[i].outputInfo())  # Because pickload(file2) is list include object of class Student
    file2.close()

    # Class Professor
    # Initialize list include object of class Professor
    professorList = [Professor() for i in range(0, 2)]
    inputClassList(professorList)
    # Sort list of professor ascending with salary
    professorList.sort(key=lambda x: x.salary)
    # Save file with Pickle
    file3 = open("D:\Professor.txt", "wb")
    pickle.dump(professorList, file3)
    file3.close()
    # Read file and print screen
    file3 = open("D:\Professor.txt", "rb")
    professorObjectList = pickle.load(file3)
    print("Professor list:")
    for i in range(0, 2):
        print(professorObjectList[i].outputInfo())
    file3.close()
if __name__ == "__main__":
    main()
