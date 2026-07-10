expenses = []
total = 0

while True:
    print("\n--- Expense Tracker ---")
    print("1. Add expense")
    print("2. View total")
    print("3. View all expenses")
    print("4. Quit")

    choice = input("Choose: ")

    if choice == "1":
        try:
            amount = float(input("Enter amount: "))
            description = input("What was it for? ")
            expenses.append({"amount": amount, "description": description})
            total = total + amount          # accumulator — this is the key concept
            print(f"✅ Added! Running total: {total:.2f}")
        except ValueError:
            print("❌ Please enter a valid number.")

    elif choice == "2":
        print(f"\n💰 Total Spent: {total:.2f}")

    elif choice == "3":
        if not expenses:
            print("No expenses yet.")
        else:
            print("\nAll Expenses:")
            for i, e in enumerate(expenses, 1):
                print(f"  {i}. {e['description']} — {e['amount']:.2f}")
            print(f"  ─────────────────")
            print(f"  TOTAL: {total:.2f}")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid option.")
