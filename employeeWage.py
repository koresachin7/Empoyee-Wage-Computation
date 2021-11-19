"""
* @Author: Sachin S Kore
* @Date: 2021-11-16
* @Title :  To check employee is present or absent using switcher also
"""
import random


class Employee:

    def check_attendance(att):
        """
          Description:
              This function is to check whether employee is present or absent.
              Employee daily wage is calculated for full day and part time.
          """

        is_full_time = 1
        is_part_time = 2
        day_Hour = 0

        wage_Per_Hour = 20
        if emp_check == is_full_time:
            day_Hour = 8
        elif emp_check == is_part_time:
            day_Hour = 4
        else:
            print("Employee is absent")

        employee_Wage = wage_Per_Hour * day_Hour
        print("Employee wage is:", employee_Wage)

    def switch(emp_check):
        absent = 0
        full_present = 1
        part_present = 2

        switcher = {
            0: absent,
            1: full_present,
            2: part_present,
        }
        attendance = switcher.get(emp_check)
        return attendance


if __name__ == "__main__":
    print("Welcome to employee wage computation")
    emp_check = random.randint(0, 2)
    att = Employee.switch(emp_check)
    Employee.check_attendance(att)

