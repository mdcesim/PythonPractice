counter = 0
mylist = "No  " + " Name " + "      Grade" + "    Latter"
print("Hello, Calculator is online")

while counter >= 0 :
    counter = counter + 1
    Name = input("Please enter the student's name: ")

    while True:
        midterm = int(input("Please input midterm grade "))
        if 0 <= midterm <= 100:
            break
        print("Error, please input correct point")

    while True:
        final = int(input("Please your final grade "))
        if 0 <= final <= 100:
            break
        print("Error, please input correct point")

    while True:
        homework = int(input("Please input homework grade "))
        if 0 <= homework <= 100:
            break
        print("Error, please input correct point ")

    x = midterm
    y = final
    z = homework

    finalgrade = x * 0.3 + y * 0.4 + z * 0.3

    print("your final grade is", finalgrade)

    if finalgrade >= 85:
        latterGrade = "A"
    elif 70 <= finalgrade < 85:
        latterGrade = "B"
    elif 50 <= finalgrade < 70:
        latterGrade = "C"
    elif 30 <= finalgrade < 50:
        latterGrade = "D"
    else :
        latterGrade = "F"
    print(latterGrade)
    mylist = mylist + "\n" + str(counter) + ".)  " + Name + "     " + str(finalgrade) + "     " + str(latterGrade)
    End = input("Press 1 to continue or press any other key to end \n")
    if End != "1" :
        break

print(mylist)
print("Calculation ended. Program is shutting down... \nGood Lock!")