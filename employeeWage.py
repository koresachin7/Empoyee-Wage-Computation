"""
* @Author: Sachin S Kore
* @Date: 2021-11-16
* @Title : To check employee Full time , part time or absent
"""
import random
print("Welcome to employee wage computation")


def check_attendance():
    """
       Description:
           This function is to check whether employee is present or absent.
           Employee daily wage is calculated for full day and part time.
       """

    isFullTime = 1
    isPartTime = 2
    day_Hour = 0

    wage_Per_Hour = 20

    emp_Check = random.randint(0, 2)

    if emp_Check == isFullTime:
        print("Employee is present Full time..... ")
        day_Hour = 8
    elif emp_Check == isPartTime:
        print("Employee is present Part time..... ")
        day_Hour = 4
    else:
        print("Employee is absent......")

    employee_Wage = wage_Per_Hour * day_Hour
    print("Employee wage is:", employee_Wage)


if __name__ == "__main__":
    check_attendance()