hourly_price = int(input("Enter price in kWh: "))
daily_usage = int(input("Enter daily use in kWh: "))
billing_period = int(input("Enter number of billing days: "))
estimated_bill = hourly_price * daily_usage * billing_period
print("Estimated bill: ${:,.2f}".format(estimated_bill))
