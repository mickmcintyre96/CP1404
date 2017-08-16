print("Electricity Bill Estimator")

TARIFF_11 = 0.244618
TARIFF_31 = 0.136928
tariff = int(input("Which tarrif are you using? 11 or 31: "))

while tariff != 11:
    print("Error, please choose one of the options")
    tariff = int(input("Which tarrif are you using? 11 or 31: "))
if tariff == 11:
    cents_per_kwh = TARIFF_11
elif tariff == 31:
    cents_per_kwh = TARIFF_31


daily_use_in_kwh = float(input("What is the daily use in kWh? "))
number_billing_days = float(input("What is the number of billing days? "))
estimated_bill = (cents_per_kwh * 100) * daily_use_in_kwh * number_billing_days
estimated_bill_in_dollars = estimated_bill / 100
print("Your estimated bill is: ${0:.2f}".format(estimated_bill_in_dollars))
