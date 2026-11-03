print("===== PERSONAL BUDGET PLANNER =====")

income = 0
expenses = []

while True:
    print("\n1. Add Income")
    print("2. Add Expense")
    print("3. View Budget")
    print("4. View Expense History")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        amount = float(input("Enter income amount: "))
        income += amount
        print("Income added successfully!")

    elif choice == "2":
        category = input("Enter expense category: ")
        amount = float(input("Enter expense amount: "))

        expenses.append({
            "category": category,
            "amount": amount
        })
        print("Expense added successfully!")

    elif choice == "3":
        total_expenses = sum(item["amount"] for item in expenses)
        balance = income - total_expenses

        print("\n===== BUDGET SUMMARY =====")
        print("Total Income:", income)
        print("Total Expenses:", total_expenses)
        print("Remaining Balance:", balance)

        print("\nExpense Details:")
        for item in expenses:
            print(item["category"], "-", item["amount"])

    elif choice=="4":
        if not expenses:
            print("No expenses recorded!")
        else:
            print("\n==== Expense History ====")
            for item in expenses:
                print(item["category"],"-",item["amount"])



    elif choice == "5":
        print("Thank you for using Budget Planner!")
        break

    else:
        print("Invalid choice!")