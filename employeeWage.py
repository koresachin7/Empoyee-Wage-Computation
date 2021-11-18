"""
* @Author: Sachin S Kore
* @Date: 2021-11-16
* @Title :  To check employee moth salary
"""
import random


def calculate_hour(attendance_status):
    """
    Description:
        This function determine the work hours
    Parameter:
        attendanceStatus is used to determine work hour of employee
    Return:
        the functution return 8 or 4 or 0 value as work hour
    """
    if attendance_status == is_full_time:
        day_Hour = 8
    elif attendance_status == is_part_time:
        day_Hour = 4
    else:
        day_Hour = 0
    return day_Hour


def get_work_hours(total_working_hours):
    '''
    Description:
        this function calculate working hours
    '''
    print("Total working hours:", total_working_hours)


def calculate_wage():
    """
    Description:
        this function calculate employee wage
    Return:
        this function return total employee wage of a month
    """
    wage_Per_Hour = 20
    working_Days = 0
    total_Working_Hours = 0
    maximum_Working_Days = 20
    maximum_Working_Hours = 100
    total_Wage = 0
    while working_Days < maximum_Working_Days and total_Working_Hours < maximum_Working_Hours:
        attendance = random.randint(0, 2)
        attendance_status = switcher.get(attendance)
        working_Hours = calculate_hour(attendance_status)
        total_Wage += working_Hours * wage_Per_Hour
        total_Working_Hours += working_Hours
        working_Days += 1
        get_work_hours(total_Working_Hours)
    return total_Wage


absent = 0
is_full_time = 1
is_part_time = 2

switcher = {
    0: absent,
    1: is_full_time,
    2: is_part_time,
}
if __name__ == '__main__':
    print("Welcome to employee wage computation")
    print("Total employee wage for month is:",calculate_wage())

