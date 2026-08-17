#challenge3 - count vowels

#input
n = input("Enter a word: ")

count = 0

for i in n:
    if i in "aeiou":
        count +=1
print("Vowel count: ",count)