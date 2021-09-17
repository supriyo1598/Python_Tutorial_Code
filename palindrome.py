str='Madam'
str=str.casefold()
rstr=reversed(str)
if list(str) == list(rstr):
    print("The string are Palindrome")
else:
    print("The string are Not Palindrome")    
