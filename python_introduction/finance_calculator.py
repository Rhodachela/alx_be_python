#User input
monthly_income = int(input("Enter your monthly income: "))
total_monthly_expenses = int(input("Enter your total monthly expenses: "))

#Calculating savings
monthly_savings = monthly_income - total_monthly_expenses

#Calculating interest
rate = 0.05
annual_savings = monthly_savings * 12
projected_savings = annual_savings + (annual_savings * rate)

print(f"Your monthly savings are: ${monthly_savings} ")
print(f"Projected annual savings after 1 year, with interest,is: ${projected_savings}")