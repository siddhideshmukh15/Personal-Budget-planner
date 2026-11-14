income = 0
expenses = []
budget = 0

while True:
    print("\n===== PERSONAL BUDGET PLANNER =====")
    print("1. Add Income")
    print("2. Add Expense")
    print("3. View Summary")
    print("4. View Expense History")
    print("5. Set Monthly Budget")
    print("6. Delete Expense")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        amount = float(input("Enter income: ₹"))
        income += amount
        print("Income added successfully!")

    elif choice == "2":
        category = input("Enter expense category: ")
        amount = float(input("Enter expense amount: ₹"))

        expenses.append([category, amount])
        print("Expense added successfully!")

        total = sum(e[1] for e in expenses)

        if budget > 0 and total > budget:
            print("Warning! Monthly budget exceeded.")

    elif choice == "3":
        total_expenses = sum(e[1] for e in expenses)
        balance = income - total_expenses

        print("\n===== BUDGET SUMMARY =====")
        print("Total Income: ₹", income)
        print("Total Expenses: ₹", total_expenses)
        print("Remaining Balance: ₹", balance)
        print("Monthly Budget: ₹", budget)

    elif choice == "4":
        print("\n===== EXPENSE HISTORY =====")

        if len(expenses) == 0:
            print("No expenses found.")
        else:
            for i, expense in enumerate(expenses, 1):
                print(i, expense[0], "- ₹", expense[1])

    elif choice == "5":
        budget = float(input("Enter monthly budget: ₹"))
        print("Budget set successfully!")

    elif choice == "6":
        for i, expense in enumerate(expenses, 1):
            print(i, expense[0], "- ₹", expense[1])

        if len(expenses) > 0:
            number = int(input("Enter expense number to delete: "))

            if 1 <= number <= len(expenses):
                expenses.pop(number - 1)
                print("Expense deleted successfully!")
            else:
                print("Invalid expense number.")
        else:
            print("No expenses to delete.")

    elif choice == "7":
        print("Thank you for using Budget Planner!")
        break

    else:
        print("Invalid choice!")