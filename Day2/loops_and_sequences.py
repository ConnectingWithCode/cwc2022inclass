def loops():
    print("----- Loops -----")

    for j in range(5):
        print(j * 10)

    total = 0
    for k in range(4 + 1):
        total = total + k
    print("Total = ", total)


def sequences():
    print("----- Sequences -----")
    ages = [6, 8, 10, 12]
    print(ages)
    print(type(ages))

    print(ages[0])
    print(ages[1])

    ages[3] = 13
    print(ages)

    ages.append(44)
    print(ages)

    total = 0
    for age in ages:
        total = total + age
    print("Total =", total)


loops()
sequences()
