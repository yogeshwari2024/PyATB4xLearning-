# Grade calculator

# write a program that calculates and displays the letter grade for a given numerical score
# eg , A, B, C, D, or F
# based on the following grading scale:

# A: 90 - 100
# B: 80 - 89
# C: 70 - 79
# D: 60 - 69
# F: 0 - 59

# logic building formula

# 1 . -> user ip -> score -> data type (int)
# 2 . -> op -> string - grade A or B...

score = int(input("Enter your score\n"))
# score >= 90 and score <= 100 -> "A"

if score >= 90 and score <= 100:
    print("your garde is", "A")

elif score >= 80 and score <= 89:
    print("your garde is", "B")

elif score >= 70 and score <= 79:
    print("your garde is", "C")

elif score >= 60 and score <= 69:
    print("your garde is", "D")

elif score >= 100:
    print("you are smart!!!")

else:
    print("grade is ", "F")
