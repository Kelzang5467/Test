print ("Hello World")
a=2
print(a>3 and a<0)
age=int(input("enter your age?: \n"))
ask=input("are you a student? (yes/no): \n")
if age<=12:
    print("you are eligible")
elif age>=13 and age==18 and ask=="yes":
    print("you are eligible")
else:
    print("not eligible")
