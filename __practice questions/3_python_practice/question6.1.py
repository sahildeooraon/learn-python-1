sentence="coading in python is fun"
# my method
a=sentence.count("a")
e=sentence.count("e")
i=sentence.count("i")
o=sentence.count("o")
u=sentence.count("u")
space=sentence.count(" ")
vovel=a+e+i+o+u
consonant=len(sentence)-(vovel+space)

print("Total no of vovel is", vovel)
print("Total no of consonant is ",consonant)

#harry method
vowel=["a","e","i","o","u"]
sum = 0
for char in sentence:
    if char in vowel:
        sum += 1
print(f"total no of vowel in sentence is {sum}")