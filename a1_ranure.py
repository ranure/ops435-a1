'''OPS435 Assignment 1 - Fall 2019
Program: a1_ranure.py (replace student_id with your Seneca User name)
Author: "Roobeera Nure"
The python code in this file (a1_ranure.py) is original work written by
"Roobeera Nure". No code in this file is copied from any other source 
except those provided by the course instructor, including any person, 
textbook, or on-line resource. I have not shared this python script 
with anyone or anything except for submission for grading.  
I understand that the Academic Honesty Policy will be enforced and 
violators will be reported and appropriate action will be taken.'''

#!/usr/bin/env python3

'''The purpose of this script is to have the user input a date, and with that date, use the many functions in the script in order to determine various results'''

import os
import sys

'''Calling the functions and letting user input'''
today = sys.argv[1]
number = sys.argv[2]

'''seperating date into 3 values'''
year = int(today[0:3])
month = int(today[5:6])
day = int(today[8:9])

def usage():
    if len(today) != 10:
       return False

def after(today):
    '''
    This function is used to return the day after the date that is given in YYYY/MM/DD format. If input is not in YYYY/MM/DD format, it will return 0000/00/00.
    '''
    if len(today) != 10:
       return '0000/00/00'
    else:
       str_year, str_month, str_day = today.split('/')
       year = int(str_year)
       month = int(str_month)
       day = int(str_day)

       lyear = year % 4
       if lyear == 0:
          feb_max = 29 # this is a leap year
       else:
          feb_max = 28 # this is not a leap year

       lyear = year % 100
       if lyear == 0:
          feb_max = 28 # this is not a leap year

       lyear = year % 400
       if lyear == 0:
          feb_max = 29 # this is a leap year

       tmp_day = day + 1 # next day

       mon_max = { 1:31, 2:feb_max, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
       if tmp_day > mon_max[month]:
          to_day = tmp_day % mon_max[month] # if tmp_day > this month's max, reset to 1
          tmp_month = month + 1
       else:
          to_day = tmp_day
          tmp_month = month + 0

       if tmp_month > 12:
           to_month = 1
           year = year + 1
       else:
           to_month = tmp_month + 0

       next_date = str(year)+"/"+str(to_month).zfill(2)+"/"+str(to_day).zfill(2)
     
       return next_date

    return next_day

def before(today):
    '''
    Function is used to return the date one day before the date that is given in YYYY/MM/DD format.
    '''
    if len(today) != 10:
       return '0000/00/00'
    else:
       str_year, str_month, str_day = today.split('/')
       year = int(str_year)
       month = int(str_month)
       day = int(str_day)

       lyear = year % 4
       if lyear == 0:
          feb_max = 29 # this is a leap year
       else:
          feb_max = 28 # this is not a leap year

       lyear = year % 100
       if lyear == 0:
          feb_max = 28 # this is not a leap year

       lyear = year % 400
       if lyear == 0:
          feb_max = 29 # this is a leap year

       tmp_day = day - 1 # next day

       mon_max = { 1:31, 2:feb_max, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
       if tmp_day > mon_max[month]:
          to_day = tmp_day % mon_max[month] # if tmp_day < this month's max, reset to 1
          tmp_month = month - 1
       else:
          to_day = tmp_day
          tmp_month = month + 0

       if tmp_month > 12:
           to_month = 1
           year = year - 1
       else:
           to_month = tmp_month + 0

       previous_date = str(year)+"/"+str(to_month).zfill(2)+"/"+str(to_day).zfill(2)
     
       return previous_date

    return previous_day

def valid_date(today):
'''Checks to see if a correct date was inputted'''
    if len(today) != 10:
       return '0000/00/00'

def leap_year(year):
'''Function checks if the year inputted is a leap year'''
    lyear = year % 4
       if lyear == 0:
       return True
       else
       return False

def days_in_mon(day):
'''Function checks how many days are in each month. Uses leap_year function to make sure'''
    if leap_year(year) == 0
       feb_max = 29
    else
       feb_max = 28
    mon_max = { 1:31, 2:feb_max, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}


def dbda(date, day):
    '''Function takes inputed date in YYYY/MM/DD format and a positive or negative integer and uses that integer to return a date before or after the inputted date'''
    setup loop:
        call after() of before() as appropriate
    return target_date

if __name__ == "__main__":
  
