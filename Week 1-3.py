
# all user inputs
hourly_rate = float(input("Enter regular hourly pay rate: "))
regular_hours = float(input("Enter total number of regular hours worked this month: "))
overtime_hours = float(input("Enter total number of overtime hours worked this month: "))
federal_tax_rate = float(input("Enter federal tax withhold percentage (e.g., 10 for 10%): ")) / 100
state_tax_rate = float(input("Enter state tax withhold percentage (e.g., 5 for 5%): ")) / 100

# overtime
overtime_rate = hourly_rate * 1.5

# gross pay
regular_gross_pay = regular_hours * hourly_rate
gross_pay = regular_gross_pay * hourly_rate + overtime_hours * overtime_rate

# tax withholds
federal_tax = gross_pay * federal_tax_rate
state_tax = gross_pay * state_tax_rate

# net pay
net_pay = gross_pay - federal_tax - state_tax

# results
print("\nPAYROLL SUMMARY")
print(f"Regular Gross Pay: ${regular_gross_pay:.2f}")
print(f"Total Gross Pay: ${gross_pay:.2f}")
print(f"Federal Tax Withheld: ${federal_tax:.2f}")
print(f"State Tax Withheld: ${state_tax:.2f}")
print(f"Net Pay: ${net_pay:.2f}")
