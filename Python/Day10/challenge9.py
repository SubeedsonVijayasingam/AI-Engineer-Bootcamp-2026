def count_numbers(numbers):
    count = {}

    for num in numbers:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1

    return count


numbers = [10, 20, 10, 30, 20, 10, 40]

result = count_numbers(numbers)

print(result)