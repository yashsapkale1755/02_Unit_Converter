python project 1

-------------------------------------

def main():
    print("=" * 35)
    print("   CLI EXPENSE & BILL SPLITTER   ")
    print("=" * 35)

    # 1. Ask for direct dollar amounts
    total_bill = float(input("\nEnter total bill amount ($): "))
    total_tip = float(input("Enter total tip amount ($): "))
    num_people = int(input("Enter number of people: "))

    # 2. Direct math calculations
    base_split = total_bill / num_people
    tip_split = total_tip / num_people
    total_per_person = base_split + tip_split
    grand_total = total_bill + total_tip

    # 3. Clear breakdown
    print("\n" + "-" * 35)
    print(f"Total Bill:        ${total_bill:.2f}")
    print(f"Total Tip:         ${total_tip:.2f}")
    print(f"Grand Total:       ${grand_total:.2f}")
    print("-" * 35)
    print(f"Base Cost / Person: ${base_split:.2f}")
    print(f"Tip Cost / Person:  ${tip_split:.2f}")
    print(f"FINAL PER PERSON:   ${total_per_person:.2f}")
    print("-" * 35)

# Replace the complicated if statement with just this single line:
main()