#challenge2 - Sum and Average

#input
n = int(input())
m = list(map(int,input().split()))

total = 0

#sum of the list
for i in m:
    total +=i
print(f"Sum: {total}")

#Average of the list
avg = sum/n
print(f"Average: {avg:.1f}")