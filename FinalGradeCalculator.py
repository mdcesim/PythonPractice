def FinalGradeCalculator():
    print("hello, calculator is online")

    midterm = int(input("Please input your midterm grade "))
    if midterm < 0 or midterm > 100:
        print("Error, please input correct point")
        midterm = int(input())

    final = int(input("Please input your final grade "))
    if final < 0 or final > 100:
        print("Error, please input correct point")
        final = int(input())

    homework = int(input("Please input your homework grade "))
    if homework < 0 or homework > 100:
        print("Error, please input correct point ")
        homework = int(input())

    x = midterm
    y = final
    z = homework

    finalgrade = x * 0.3 + y * 0.4 + z * 0.3

    print("your final grade is", finalgrade)

    if finalgrade >= 85:
        print("A")
    if 70 <= finalgrade < 85:
        print("B")
    if 50 <= finalgrade < 70:
        print("C")
    if 30 <= finalgrade < 50:
        print("D")
    if finalgrade < 30:
        print("F,", "You failed. See you next year :)")
        
    End = input("Press R to restart calculation or press any button to end ")
    if End == "R" or End == "r":
        FinalGradeCalculator()
    else: 
        print("Calculation ended. Good lock!")


FinalGradeCalculator() 