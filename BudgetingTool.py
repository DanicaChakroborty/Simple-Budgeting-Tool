'''
Name: Danica Chakroborty
Date: December 20th
Project: Simple budgeting tool, created for fun as a side project
'''


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

def export_to_csv(income, expenses, total_expenses, net_income):
    #open file named my_budget.csv in write mode
    try:
        with open('budget.csv', 'w') as file:
            # csv formatting
            file.write("Budget Summary\n")
            file.write("-----------------\n\n")
            file.write(f"Monthly Income: ${income:.2f}\n\n") # income
            file.write("EXPENSES:\n")
            file.write("---------\n")
            for category, amount in expenses.items():
                percentage = (amount / income * 100) if income > 0 else 0
                file.write(f"{category}: ${amount:.2f} ({percentage:.1f}%)\n") # all expenses with percentage
            file.write("\nSUMMARY:\n")
            file.write("--------\n")
            file.write(f"Total Expenses: ${total_expenses:.2f}\n") # expense total
            file.write(f"Net Income: ${net_income:.2f}\n") #net income
        
        print("\nYour budget has been saved to 'budget.csv'!")
    except:
        print("\nThere was an error saving your budget.")

def main():
    print("Welcome to your personal budgeting tool!")
    income = get_income()
    expenses = get_expenses()
    net_income, total_expenses = calculate_net_income(income, expenses)
    display_breakdown(income, expenses, total_expenses, net_income)
    export_choice = input("\nWould you like to export this budget to a CSV file? (yes/no): ").lower()
    if export_choice.startswith('y'):
        export_to_csv(income, expenses, total_expenses, net_income)

if __name__ == "__main__":
    main()