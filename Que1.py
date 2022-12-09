import re

number = input("Enter Number: ")
Pattern = re.compile("(212|121|1)?[-\s.]?[4-6][0-9]")


if Pattern.match(number):
    print(f"{number} is Valid Contact Number")

else:
    print(f"{number} is Not Valid Contact Number")



# Input Checked

# 2124567890
# 212-466-7890
# 212.456.7890
# 212 456 7890
# 
