TARIFF_11 = 0.244618
TARIFF_31 = 0.136928

tariff = input("Which tariff? 11 or 31: ")
while tariff != "11" and tariff != "31":
    print("Please select a valid tariff")
    tariff = input("Which tariff? 11 or 31: ")
if tariff == "11":
    hourly_price = TARIFF_11
else:
    hourly_price = TARIFF_31
daily_usage = int(input("Enter daily use in kWh: "))
billing_period = int(input("Enter number of billing days: "))
estimated_bill = hourly_price * daily_usage * billing_period
print("Estimated bill: ${:,.2f}".format(estimated_bill))
