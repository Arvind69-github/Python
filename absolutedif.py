x: int = int(input("enter a number that should be greater than 17: "))
if x > 17:
    diff: int = x - 17
    print(diff + diff)
else:
    print("Number is smaller than 17")