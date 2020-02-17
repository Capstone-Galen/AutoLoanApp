import decimal as dc
# Auto Loan Calculator console representation
# Created by Galen Schatzman 12/26/2019
#Now added to repository at https://github.com/SchatzmanGPS/ConsoleLoanApp.git
print("")
print("*************************************************************************")
print("*************************************************************************")
print("************** AUTO LOAN CALCULATOR CONSOLE APPLICATION *****************")
print("*************************************************************************")
print("*************************************************************************")
print("")
g = input("Enter the amount in dollars you would like to borrow from the bank: ")
g = dc.Decimal(g)
h = input("Enter the loan interest rate (i.e. 4.49): ")
h = dc.Decimal(h)
i = input("Enter the term of your loan in years: ")
i = dc.Decimal(i)

#print("Calculating your loan inquiry")
print("Calcutating...")
print("")
interestRate = (h / 100)
interestRate = dc.Decimal(interestRate)
monthCalc = (i * 12)
monthCalc = dc.Decimal(monthCalc)
interestXComp = (interestRate / 1)
interestXComp = dc.Decimal(interestXComp)
a = (1 + interestXComp)
b = (1 * i)
#POW = pow(a,b) Line 23 is also a exponential expression
POW = (a**b)
totalCost = (g * POW)
tc = round(totalCost, 2)
interestCost = (totalCost - g)
ic = round(interestCost, 2)
monthly = (totalCost / monthCalc)
m = round(monthly, 2)
#Convert above values to strings below
tc = str(tc)
ic = str(ic)
m = str(m)
monthCalc = str(monthCalc)

print("")
print("The total cost of your loan is: $" + tc)
print("")
print("The cost of interest at the time of the loan is: $"+ ic)
print("")
print("Your minimum monthly payment will be: $" + m)
print("")
print("You will be paying the above amount for " + monthCalc + " months.")
print("")


