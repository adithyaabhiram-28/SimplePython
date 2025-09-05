name = input("Enter your of Student name: ")
number = input("Enter your roll number: ")
c,java,cpp = map(int, input("Enter marks of 3 subjects: ").split())
total = c + java + cpp
avg = total / 3
round(avg, 2)
print("Name:", name)
print("Roll Number:", number)
print("Total Marks:", total)
print("Average Marks:", avg)




if(avg > 80):
    print("Distinction")
elif(avg > 70 and avg <=80):
    print("A Grade")
elif(avg > 50 and avg <=70):
    print("B Grade")
elif(avg > 40 and avg <=50):
    print("C Grade")
else:
    print("Fail")
    