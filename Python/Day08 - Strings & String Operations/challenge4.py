#challenge4 - count upper and lowercase

#input
n = input("Enter a words: ")

#count
upper_count = 0
lower_count = 0

for i in n:
    if i.islower() :
        lower_count +=1
    elif i.isupper():
        upper_count +=1
print(f"Uppercase count: {upper_count}")
print(f"Lowercase count: {lower_count}")
