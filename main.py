print("Hope you enjoyed your dinner\nAnd welcome to the tip calculator")
bill = float(input("Enter the bill amount($): "))
tip = int(input("Enter the tip percentage: "))
people = int(input("Enter the number of people to split the bill between: "))
final_bill = (bill * (1 + tip/100)) / people
print(f"The bill per person is ${round(final_bill, 2)}\nThank You for Using Our App")
