#challenge1 - List basics

n = int(input())
numbers = list(map(int, input().split()))

print(f"List: {numbers}")
print(f"First: {numbers[0]}")
print(f"Last: {numbers[-1]}")
print(f"Length: {len(numbers)}")