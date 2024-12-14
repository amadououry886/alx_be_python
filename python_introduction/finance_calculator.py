#This for to calculate finance.
monthly_income = float(input("Enter you monthly income :"))
monthly_expenses = float(input("Enter your total monthly expenses :"))
monthly_savings = monthly_income - monthly_expenses

print(f"Your monthly savings are ${monthly_savings}.")
project_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)

print(f"Projected savings after one year, with interest, is : ${project_savings}.")

