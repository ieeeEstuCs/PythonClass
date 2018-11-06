IEEE=["cs","ras","wie","cis","aess"]
numberOfMember=[105,25,40,35,50]
for i in range(0,len(IEEE)):
    print(IEEE[i],numberOfMember[i])

# ------------------
i = 1
total = 0
while (i < 50):
    total += i  # total = total+i
    i += 1
print(total)
# ----------------
total = 0
for i in range(50):
    total += i
# n*(n+1)/2=sum
print(total)
#------------------
fac = int(input("Enter a number: "))
multi = 1
for i in range(1, fac + 1):
    multi *= i
print(multi)
#------------------
userInput = input()
i=0
sum=0
while(i<len(userInput)):
    sum+=int(userInput[i])
    i+=1
print(sum)