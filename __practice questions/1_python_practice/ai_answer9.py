a = "python code must always end with a semicolon ;"
b = "The # symbol is used for comments in Python."
c = '"123" and 123 are the same in Python.'
d = "The * operator is used for multiplication."
e = "\\n creates a new line."
f = "Variables in Python can start with numbers."
g = 'int("10") + 5 gives 15'

score = 0

answer1 = input(a + " True or False: ")
answer2 = input(b + " True or False: ")
answer3 = input(c + " True or False: ")
answer4 = input(d + " True or False: ")
answer5 = input(e + " True or False: ")
answer6 = input(f + " True or False: ")
answer7 = input(g + " True or False: ")

if answer1.lower() == "false":
    score += 1
if answer2.lower() == "true":
    score += 1
if answer3.lower() == "false":
    score += 1
if answer4.lower() == "true":
    score += 1
if answer5.lower() == "true":
    score += 1
if answer6.lower() == "false":
    score += 1
if answer7.lower() == "true":
    
    score += 1


# Continue the same pattern for answer2 through answer7

print("Your score is:", score, "/ 7")
