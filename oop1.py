"""
This script defines the University and Department classes to represent 
universities and their departments.
"""
class University:
    """
    A class representing a university.
    """
    def __init__(self, name: str, location: str):
        """
        Initialize a University object.

        Parameters:
        name (str): The name of the university.
        location (str): The location of the university.

        Returns:
        None
        """
        self.__name = name
        self.__location = location
        self.__departments = []

    def add_department(self, department: 'Department') -> None:
        """
        Add a department to the university.

        Parameters:
        department (Department): The department to be added.

        Returns:
        None
        """
        self.__departments.append(department)

    def display_details(self) -> None:
        """
        Display the details of the university, including its departments.

        Parameters:
        None

        Returns:
        None
        """
        print(f"University Name: {self.__name}")
        print(f"Location: {self.__location}")
        print("Departments:")
        for department in self.__departments:
            department.display_details()


class Department(University):
    """
    A class representing a department within a university.
    """
    def __init__(self, university_name: str, university_location: str,
                 department_name: str, head_of_department: str):
        """
        Initialize a Department object.

        Parameters:
        university_name (str): The name of the university.
        university_location (str): The location of the university.
        department_name (str): The name of the department.
        head_of_department (str): The head of the department.

        Returns:
        None
        """
        super().__init__(university_name, university_location)
        self.__department_name = department_name
        self.__head_of_department = head_of_department
        self.__courses_offered = []

    def add_course(self, course: str) -> None:
        """
        Add a course to the department.

        Parameters:
        course (str): The course to be added.

        Returns:
        None
        """
        self.__courses_offered.append(course)

    def display_details(self) -> None:
        """
        Display the details of the department, including its courses.

        Parameters:
        None

        Returns:
        None
        """
        super().display_details()
        print(f"Department: {self.__department_name}")
        print(f"Head of Department: {self.__head_of_department}")
        print("Courses Offered:")
        for course in self.__courses_offered:
            print(f"- {course}")

# Creating instances
university = University("Tribhuvan University", "Kathmandu")
department = Department("Tribhuvan University", "Kathmandu",
                        "Computer Science", "Dr. Bal Krishna Bal")

# Adding departments and courses
university.add_department(department)
department.add_course("Introduction to Programming")
department.add_course("Data Structures and Algorithms")

# Displaying details
university.display_details()
print("\n")
department.display_details()
