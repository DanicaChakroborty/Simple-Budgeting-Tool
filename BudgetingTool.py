def get_income():
    
    while True:
        try:
            income = float(input("Enter your total monthly income: "))
            if income < 0:
                raise ValueError("Income cannot be negative, sorry!")
            return income
        except ValueError as e:
            print(f"Invalid input: {e}. Please enter a positive number, thank you")

def get_expenses():
    
    expenses = {}
    print("Enter your monthly expenses. Type 'done' when finished!")
    while True:
        category = input("Expense category (e.g., Rent, Food, Utilities): ").strip()
        if category.lower() == 'done':
            break
        try:
            amount = float(input(f"Amount for {category}: "))
            if amount < 0:
                raise ValueError("Expense cannot be negative, sorry!")
            expenses[category] = expenses.get(category, 0) + amount
        except ValueError as e:
            print(f"Invalid input: {e}. Please enter a positive number, thank you")
    return expenses

def calculate_net_income(income, expenses):
    
    total_expenses = sum(expenses.values())
    return income - total_expenses, total_expenses

def display_breakdown(income, expenses, total_expenses, net_income):
   
    print("\n===== Budget Summary =====")
    print(f"Total Income: ${income:.2f}")
    print("\nExpenses:")
    for category, amount in expenses.items():
        percentage = (amount / income * 100) if income > 0 else 0
        print(f"  {category}: ${amount:.2f} ({percentage:.1f}%)")
    print(f"\nTotal Expenses: ${total_expenses:.2f}")
    print(f"Net Income: ${net_income:.2f}")
    if net_income > 0:
        print("You have a surplus. Consider saving or investing it!")
    elif net_income < 0:
        print("Uh-oh! You are overspending!! Consider adjusting your expenses, yikes!")
    else:
        print("Your budget is perfectly balanced, yippee!!")

def main():
    
    print("Welcome to your personal budgeting tool!")
    income = get_income()
    expenses = get_expenses()
    net_income, total_expenses = calculate_net_income(income, expenses)
    display_breakdown(income, expenses, total_expenses, net_income)

if __name__ == "__main__":
    main()