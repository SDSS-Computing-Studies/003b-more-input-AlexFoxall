#!python3
 
"""
##### Task 1
The bank calculates the amount of interest you earn using the simple interest formula:
interest = principal * rate * #days in the month / 365

Ask the user to enter the amount of their principal, the number of days in the month the rate of interest expressed as a percentage.  Calculate the amount of interest they would be paid.

example:
Enter your amount: 100
Enter the rate: 2.5
Enter the # of days in the month: 30
You earned $0.20 interest. 
(2 points) 
"""
import math

x = float(input("enter your principle"))
y = float(input("enter number of days in month"))
b = float(input("enter intrest as a percent"))
b = b / 100
xyb = x * b * y
num = xyb / 365
num = num * 10
num = round(num)
num= num / 10
num = str(num)
print("You earned $" + num + " interest.")