#3. write a python code to check a year is a leap year or not .

year=int(input("Enter a year for leap year check: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a leap year")
else:
    print(year, "is not a leap year")