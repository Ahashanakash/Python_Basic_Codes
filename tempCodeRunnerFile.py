n = int(input())
ar = input()
arr = list(map(int, ar.split()))

# Initialize a dictionary to store frequencies
frequency = {}

# Manually count occurrences of each element in arr
for num in arr:
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1
print(frequency)