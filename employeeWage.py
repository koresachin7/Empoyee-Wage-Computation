"""
* @Author: Sachin S Kore
* @Date: 2021-11-15
* @Title : To employee wage welcome sms
"""
import random
print("Welcome to employee wage computation")

def check_attendance():
    """
    Description:
        This function is to check whether employee is present or absent.
    """

    emp_Check = random.randint(0,1)

    if emp_Check == 0:
        print("Employee is present")
    else:
        print("Employee is absent")

if __name__ == "__main__":
    check_attendance()