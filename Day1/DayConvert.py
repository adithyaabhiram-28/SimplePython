def convert_days(days):
    years = days / 365
    remaining_days = days % 365
    months = remaining_days / 30
    return years, months
days = int(input("Enter number of days: "))
years, months = convert_days(days)
print(f"{days} days is approximately {years} years and {months} months.")