#3. write a python program to check if a string is palindrome or not .
original_string=input("Enter a string : ")
reverse_string=original_string[::-1]

if original_string == reverse_string:
    print("The string is palindrome string !")
else:
    print("The string is not a palindrome string !")