# remove 3 lowest scores and output sum of rest.

numbers = input()

numbers = numbers.split(" ")
floatss = [float(x) for x in numbers]

count = 0
for num in floatss:
    count += 1
if count < 3:
    print("At least 3 scores needed!")
else:
    floatss.sort(reverse=True)
    floatss.pop()
    floatss.pop()
    floatss.pop()
    print(f"Sum of scores (3 lowest removed): {round(sum(floatss), 1)}")