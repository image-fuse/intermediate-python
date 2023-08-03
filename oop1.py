class University:
    def __init__(self, name, location):
        self.__name = name
        self.__location = location
        self.__departments = []
        
    def add_department(self, department):
        self.__departments.append(department)
        
    def display_details(self):
        print(f"University Name: {self.__name}")
        print(f"Location: {self.__location}")
        print("Departments:")
        for department in self.__departments:
            print(f"- {department.get_department_name()}")

class Department(University):
    def __init__(self, name, location, department_name, head_of_department):
        super().__init__(name, location)
        self.__department_name = department_name
        self.__head_of_department = head_of_department
        self.__courses_offered = []
        
    def add_course(self, course):
        self.__courses_offered.append(course)
        
    def get_department_name(self):
        return self.__department_name
        
    def display_details(self):
        super().display_details()
        print(f"Department: {self.__department_name}")
        print(f"Head of Department: {self.__head_of_department}")
        print("Courses Offered:")
        for course in self.__courses_offered:
            print(f"- {course}")

# Creating instances
university = University("Tribhuvan University", "Kathmandu")
department = Department("Kathmandu University", "Dhulikhel", "Computer Science", "Dr. Bal Krishna Bal")

# Adding departments and courses
university.add_department(department)
department.add_course("Introduction to Programming")
department.add_course("Data Structures and Algorithms")

# Displaying details
university.display_details()
print("\n")
department.display_details()
