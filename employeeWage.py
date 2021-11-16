"""
* @Author: Sachin S Kore
* @Date: 2021-11-16
* @Title : To calculate the employee daily wage
"""
import random
print("Welcome to employee wage computation")


def check_attendance():
    """
    Description:
        This function is to check whether employee is present or absent.
        Employee daily wage is calculated for full day.
    """

    wage_Per_Hour = 20

    emp_Check = random.randint(0, 1)

    if emp_Check == 0:
        print("Employee is present")
        full_day_Hour = 8
    else:
        print("Employee is absent")

    employee_Wage = wage_Per_Hour * full_day_Hour
    print("Employee wage is:", employee_Wage)


if __name__ == "__main__":
    check_attendance()