#User input
monthly_income = int(input("Enter your monthly income: "))
monthly_expenses = int(input("Enter your total monthly expenses: "))

#Calculating savings
monthly_savings = monthly_income - monthly_expenses

#Calculating interest
projected_savings = monthly_savings * 12 + (monthly_savings *12 * 0.05)

print(f"Your monthly savings are: ${monthly_savings}")
print(f"Projected annual savings after 1 year, with interest,is: ${projected_savings}")