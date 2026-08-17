#challenge5 - List analyzer

#input
n = int(input())
m = list(map(int,input().split()))

#sum
total = 0
for i in m:
    total +=i

#count
even_count = 0
odd_count = 0

for i in m:
    if i%2 == 0:
        even_count +=1
    else:
        odd_count +=1

#output
print(f"Sum: {total}")
print(f"Maximum: {max(m)}")
print(f"Minimum: {min(m)}")
print(f"Even count: {even_count}")
print(f"Odd count: {odd_count}")