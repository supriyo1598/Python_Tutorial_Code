string = input("Enter any string : ")
lst = list(string)
n = int(input("Enter the n : "))
print("You have removed : ", lst.pop(n))
string = "".join(lst)
print("Now String is: '{}' ".format(string))
