"""
* @Author: Sachin S Kore
* @Date: 2021-11-16
* @Title :  To check employee moth salary
"""
import random


def calculateHour(attendanceStatus):
    """
    Description:
        This function determine the work hours
    Parameter:
        attendanceStatus is used to determine work hour of employee
    Return:
        the functution return 8 or 4 or 0 value as work hour
    """
    if attendanceStatus == isFullTime:
        day_Hour = 8
    elif attendanceStatus == isPartTime:
        day_Hour = 4
    else:
        day_Hour = 0
    return day_Hour

def calculateWage():
    """
    Description:
        this function calculate employee wage
    Return:
        this function return total employee wage of a month
    """
    wage_Per_Hour = 20
    working_Days = 20
    total_Wage = 0
    for day in range(working_Days):
        attendance = random.randint(0,2)
        attendanceStatus = switcher.get(attendance)
        workingHours = calculateHour(attendanceStatus)
        total_Wage += workingHours * wage_Per_Hour
    return total_Wage

absent = 0
isFullTime = 1
isPartTime = 2

switcher = {
    0: absent,
    1: isFullTime,
    2: isFullTime,
}
if __name__ == '__main__':
    print("Welcome to employee wage computation")
    print("Total employee wage for month is:",calculateWage())

