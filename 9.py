'''Exercises
You Are Going to make a love calculator for two person.
'''
print("Welcome to Love Calculator")
name1 = input("What Is Your Name? \n")
name2 = input("What Is Their Name? \n")

lower_case_name1 = name1.lower()
a = lower_case_name1.count("t")
b  = lower_case_name1.count("r")
c  = lower_case_name1.count("u")
d  = lower_case_name1.count("e")
print(f"T occur in name1 {a}")
print(f"R occur in name1 {b}")
print(f"U occur in name1 {c}")
print(f"E occur in name1 {d}")
total_true = a + b + c + d

print(f"Total True Occur :{total_true}")

lower_case_name2 = name2.lower()
x = lower_case_name2.count("l")
y  = lower_case_name2.count("o")
z  = lower_case_name2.count("v")
w  = lower_case_name2.count("e")
print(f"L occur in name1 {x}")
print(f"O occur in name1 {y}")
print(f"V occur in name1 {z}")
print(f"E occur in name1 {w}")
total_love = x + y + z + w

print(f"Total Love occur : {total_love}")

love_score = int(str(total_true) + str(total_love))
print(f"Your Love Score is : {love_score}")
print("\n")


if (love_score < 10) or (love_score > 90):
    print(f"Your Score is {love_score} and You Both are like Coke and Mentos..")
elif (love_score > 40) and (love_score < 50):
    print(f"Your Score is {love_score} , you are alright together")
else:
    print(f"Your Score is : {love_score}")
