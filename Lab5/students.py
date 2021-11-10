course_settings_dict_test = {
    'max_amout_of_marks_for_individual_project': 100,
    'max_mark_per_one_lab': 5,
    'amount_of_labs_in_course': 10,
    'total_amout_for_auto_mark': 92
}


class Student():

    def __init__(self, student_name, course_settings_dict):
        self.student_name = student_name
        self.course_settings_dict = course_settings_dict

        self.lab_tries = 0
        self.ind_project_tries = 0

        self.total_lab_marks = 0
        self.total_individual_marks = 0

    def add_mark_for_last_lab_try(self, mark):
        self.total_lab_marks += mark

    def add_amout_of_tries_to_pass_lab(self, amount, mark):
        self.lab_tries = amount
        self.add_mark_for_last_lab_try(mark)

    def add_amout_of_tries_to_pass_ind_project(self, amount, mark):
        self.ind_project_tries = amount
        self.add_mark_for_last_ind_project_try(mark)

    def add_mark_for_last_ind_project_try(self, mark):
        self.total_individual_marks += mark

    def get_student_report(self):
        amount_of_marks = self.total_lab_marks + self.total_individual_marks
        is_auto_mark = False

        if amount_of_marks >= self.course_settings_dict['total_amout_for_auto_mark']:
            is_auto_mark = True

        result_turple = (amount_of_marks, is_auto_mark)
        return result_turple


student = Student("Pasha", course_settings_dict_test)

amount_of_tries = input("Amout of lab tries: ")
last_lab_mark = input("Last lab mark: ")

student.add_amout_of_tries_to_pass_lab(int(amount_of_tries), int(last_lab_mark))

amount_of_ind_tries = input("Amout of individual project tries: ")
last_ind_mark = input("Last individual project mark: ")

student.add_amout_of_tries_to_pass_ind_project(int(amount_of_ind_tries), int(last_ind_mark))

result_turple = student.get_student_report()
print('Total marks: ' + str(result_turple[0]) + ' Is auto mark: ' + str(result_turple[1]))
