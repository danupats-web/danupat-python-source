print("1. THB to USD")
print("2. USD to THB")

choice = input("Enter your choice: ")

if choice == "1":
    thb = float(input("Enter amount in THB: "))
    usd = thb / 35.5
    print("Formula:", thb, "/ 35.5 =", round(usd, 2))
    print("USD =", round(usd, 2))

elif choice == "2":
    usd = float(input("Enter amount in USD: "))
    thb = usd * 35.5
    print("Formula:", usd, "* 35.5 =", round(thb, 2))
    print("THB =", round(thb, 2))

else:
    print("Invalid choice")