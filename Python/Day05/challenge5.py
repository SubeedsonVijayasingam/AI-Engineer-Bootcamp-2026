#challenge5

n = int(input("Enter a number: "))
print("==== NUMBER ANALYZER ====")

#sum of all numbers

total = 0
for i in range(1, n+1):
    total +=i
print(f"Sum: {total}")

#count of even numbers

count_even = 0
for  i in range(1, n+1):
    if i%2 == 0:
        count_even +=1
print(f"Even count: {count_even}")

#count of odd numbers
count_odd = 0
for i in range(1, n+1):
    if i%2 != 0:
        count_odd +=1
print(f"Odd count: {count_odd}")

#sum of even numbers

total_even = 0
for i in range(1, n+1):
    if i%2 == 0:
        total_even += i
print(f"Even sum: {total_even}")

#sum of odd numbers

total_odd = 0
for i in range(1, n+1):
    if i%2 != 0:
        total_odd +=i
print(f"Odd sum: {total_odd}")