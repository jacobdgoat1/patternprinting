rows = int(input("How many rows"))
for row in range(1, rows + 1):
    for star in range(1, row + 1):
        print("* ", end="")
    print()

