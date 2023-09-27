def closestNumbers(numbers):
    # Write your code here
    numbers.sort()
    closest = []
    min_n = numbers[1] - numbers[0]
    for number in range(2, len(numbers)):
        min_n = min(min_n, numbers[number] - numbers[number - 1])
    for number in range(1, len(numbers)):
        if numbers[number] - numbers[number - 1] == min_n:
            closest.append(numbers[number - 1])
            closest.append(numbers[number])

    for i in range(0, len(closest), 2):
        print(f"{closest[i]} {closest[i + 1]}")

