#challenge5 - string analyzer

#input
text = input("Enter a word: ")

#Reverse
m = text[::-1]

#Length of the string
l = len(text)

#vowel count
count = 0
for i in text:
    if i in "aeiouAEIOU":
        count +=1

#Upper and lowercase count
upper_count = 0
lower_count = 0
for i in text:
    if i.isupper():
        upper_count +=1
    elif i.islower():
        lower_count +=1

#Output
print(f"Original: {text}")
print(f"Reverse: {m}")
print(f"Length: {l}")
print(f"Vowel count: {count}")
print(f"Uppercase count: {upper_count}")
print(f"Lowercase count: {lower_count}")