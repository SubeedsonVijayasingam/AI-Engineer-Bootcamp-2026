#challenge4 - count Even and Odd

#input
n = int(input())
m = list(map(int,input().split()))

#count
even_count = 0
odd_count = 0

for i in  m:
    if i%2==0:
        even_count +=1
    else:
        odd_count +=1

#output
print(f"Even count: {even_count}")
print(f"Oddcount: {odd_count}")