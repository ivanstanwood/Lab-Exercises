import time
grade_dict = {}
count = 0

class StudentRecord:
    def __init__(self, personal_info, grade_list, GPA_thing):
        self.personal_info = personal_info
        self.grade_list = grade_list
        self.GPA_thing = GPA_thing
    def write_personal_info(self):
        return self.personal_info
    def write_grade_list(self):
        grade_dict.update(self.grade_list)
        return self.grade_list
    def write_GPA(self):
        return self.GPA_thing

def get_info():
    info = input("Tell me a little bit about yourself: ")
    return info 
def get_grades():
    grades_class_statement = input("For what class would you like to add grades for? ")
    grades_grade_statement = input("What grade did you get in this class? ")
    grades = {grades_class_statement: grades_grade_statement}
    return grades
def get_gpa():
    gpa = input("What is your current GPA? ")
    return gpa

d1 = StudentRecord(get_info(), get_grades(), get_gpa())

while count == 0:
    function_input = int(input("Would you like to access 1: Your Personal Info, 2: Your Class Grades, or 3: Your GPA? "))
    if function_input == 1:
        print(d1.write_personal_info())
    elif function_input == 2:
        print(grade_dict)
    elif function_input == 3:
        print(d1.write_GPA())
    else:
        print("That is not an option!")
    time.sleep(1)
    print("")
    continue_input = input("Would you like to input anything else? ")
    if continue_input == "yes" or continue_input == "Yes":
        count = 0
        modify_answer = int(input("Which file would you like to modify, 1: Your Personal Info, 2: Your Class Grades, or 3: Your GPA? "))
        if modify_answer == 1:
            get_info()
            d1.write_personal_info()
        if modify_answer == 2:
            grade_dict.update(get_grades())
        if modify_answer == 3:
            get_gpa()
            d1.write_GPA()
    elif continue_input == "no" or continue_input == "No":
        print("Thank you! Come again")
        count += 1
    else:
        print("That's not an option!")
