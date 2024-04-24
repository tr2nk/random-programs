from math import sqrt
while True:
    a = int(input("Enter the A value: "))
    b = int(input("Enter the B value: "))
    c = int(input("Enter the C value: "))

    output1 = str((-b + sqrt(int(str(b ** 2 - 4 * a * c).replace("-", "")))) / (2 * a)) + ("i" if str(b ** 2 - 4 * a * c) != str(b ** 2 - 4 * a * c).replace("-", "") else "")
    output2 = str((-b - sqrt(int(str(b ** 2 - 4 * a * c).replace("-", "")))) / (2 * a)) + ("i" if str(b ** 2 - 4 * a * c) != str(b ** 2 - 4 * a * c).replace("-", "") else "")

    print(output1)
    print(output2)

    print(f"\n-{b} +- sqrt({b ** 2 - 4 * a * c})".replace("--", "+"))
    print("-" * len(f"\n-{b} +- sqrt({b ** 2 - 4 * a * c})".replace("--", "")))
    print(" " * (len(f"\n-{b} +- sqrt({b ** 2 - 4 * a * c})".replace("--", ""))// 2 - 1) + f"{2 * a}")