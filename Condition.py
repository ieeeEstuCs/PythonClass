# userInput=int (input("Enter a number: "))
# if userInput is 10:
#     print("Ok")
# else:
#     print("Not Ok")
userInput = int(input("Enter your grade"))
if userInput<=100 and userInput>=0:
    if userInput >= 90:
        print("AA")
    elif userInput >= 80:
        print("BB")
    elif userInput >= 70:
        print("CC")
    elif userInput >= 60:
        print("DD")
    else:
        print("FF")
else:
    print("Enter a number which should be greater than 0 and less than 100")



userInput = int(input("Enter a number: "))
if userInput %2 == 0:
    print("Number is Even")
else:
    print("Number is Odd")
