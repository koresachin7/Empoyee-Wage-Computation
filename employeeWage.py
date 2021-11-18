"""
* @Author: Sachin S Kore
* @Date: 2021-11-16
* @Title :  To check employee is present or absent using switcher also
"""
import random


class Employee:

    def check_attendance(e):
        """
          Description:
              This function is to check whether employee is present or absent.
              Employee daily wage is calculated for full day and part time.
          """

        isFullTime = 1
        isPartTime = 2
        day_Hour = 0

        wage_Per_Hour = 20
        if emp_check == isFullTime:
            day_Hour = 8
        elif emp_check == isPartTime:
            day_Hour = 4
        else:
            print("Employee is absent")

        employee_Wage = wage_Per_Hour * day_Hour
        print("Employee wage is:", employee_Wage)

    def switch(x):
        absent = 0
        full_present = 1
        part_present = 2

        switcher = {
            0: absent,
            1: full_present,
            2: part_present,
        }
        attendance = switcher.get(emp_check)
        print(attendance)


if __name__ == "__main__":
    print("Welcome to employee wage computation")
    emp_check = random.randint(0, 2)
    a = Employee()
    a.check_attendance()
    a.switch()
