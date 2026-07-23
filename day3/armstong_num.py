#1. write a python code to check if a given number is Armstong No or not .

# what is armostrong number -- example 153 = 1^3 + 5^3 + 3^3 = 153
num=int(input("Enter a number for Armstrong check: "))
sum=0
temp=num
while temp>0:
    digit=temp%10
    sum+=digit**3
    temp//=10

if num == sum:
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")