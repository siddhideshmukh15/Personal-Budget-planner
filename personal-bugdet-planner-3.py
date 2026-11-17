income = 0
expenses = []
budget = 0

while True:
    print("\n===== PERSONAL BUDGET PLANNER =====")
    print("1. Add Income")
    print("2. Add Expense")
    print("3. View Budget Summary")
    print("4. View Expense History")
    print("5. Set Monthly Budget")
    print("6. Delete Expense")
    print("7. Search by Category")
    print("8. Show Highest Expense")
    print("9. Category-wise Spending")
    print("10. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        amount = float(input("Enter income: ₹"))

        if amount > 0:
            income += amount
            print("Income added successfully!")
        else:
            print("Enter a valid amount.")

    elif choice == "2":
        category = input("Enter expense category: ")
        amount = float(input("Enter expense amount: ₹"))

        if amount > 0:
            expenses.append([category, amount])
            print("Expense added successfully!")

            total = sum(e[1] for e in expenses)

            if budget > 0 and total > budget:
                print("Warning! Monthly budget exceeded.")
        else:
            print("Enter a valid amount.")

    elif choice == "3":
        total_expenses = sum(e[1] for e in expenses)
        balance = income - total_expenses

        print("\n===== BUDGET SUMMARY =====")
        print("Total Income: ₹", income)
        print("Total Expenses: ₹", total_expenses)
        print("Remaining Balance: ₹", balance)
        print("Monthly Budget: ₹", budget)

        if budget > 0:
            print("Budget Remaining: ₹", budget - total_expenses)

    elif choice == "4":
        print("\n===== EXPENSE HISTORY =====")

        if len(expenses) == 0:
            print("No expenses found.")
        else:
            for i, expense in enumerate(expenses, 1):
                print(i, expense[0], "- ₹", expense[1])

    elif choice == "5":
        amount = float(input("Enter monthly budget: ₹"))

        if amount > 0:
            budget = amount
            print("Monthly budget set successfully!")
        else:
            print("Enter a valid budget.")

    elif choice == "6":
        if len(expenses) == 0:
            print("No expenses to delete.")
        else:
            for i, expense in enumerate(expenses, 1):
                print(i, expense[0], "- ₹", expense[1])

            number = int(input("Enter expense number to delete: "))

            if 1 <= number <= len(expenses):
                removed = expenses.pop(number - 1)
                print("Deleted:", removed[0])
            else:
                print("Invalid expense number.")

    elif choice == "7":
        category = input("Enter category to search: ")
        found = False

        for expense in expenses:
            if expense[0].lower() == category.lower():
                print(expense[0], "- ₹", expense[1])
                found = True

        if not found:
            print("No expenses found in this category.")

    elif choice == "8":
        if len(expenses) == 0:
            print("No expenses found.")
        else:
            highest = max(expenses, key=lambda x: x[1])
            print("Highest Expense:", highest[0], "- ₹", highest[1])

    elif choice == "9":
        category = input("Enter category: ")
        total = 0

        for expense in expenses:
            if expense[0].lower() == category.lower():
                total += expense[1]

        print("Total spending on", category, "is ₹", total)

    elif choice == "10":
        print("Thank you for using Budget Planner!")
        break

    else:
        print("Invalid choice! Try again.")