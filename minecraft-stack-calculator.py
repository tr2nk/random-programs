from math import floor

while True:
    try:
        _in = int(input("Enter the amount: "))
        shulkers = floor(_in / 64 / 27)
        stacks = floor((_in / 64) % 27)
        extra = floor(_in % 24 % 64 )

        if shulkers:
            print(str(shulkers) + " shulker" + ("s" if shulkers != 1 else ""), end = ", ")
        print(str(stacks) + " stack" + ("s" if stacks != 1 else "") + " and " + str(extra))
    except:
        print("Bad input.")