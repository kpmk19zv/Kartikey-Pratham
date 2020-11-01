print('To calculate your Tax ! Enter the Following details')

'Getting Details from user '

total_income = int(input('Enter your total income ie per annum in Rs:'))
age = int(input('Enter age :'))
sex = str(input("Enter sex (M or F) :"))
investment_amount = int(input('Enter your investment amount in Rs:'))

# if salary up to Rs.2,50,000
if total_income <= 250000 and age < 60:
    taxable_income = total_income - investment_amount  # Deducting the investment amount from total income
    taxable_income = (taxable_income - (taxable_income * .04))  # Deducting 4% of Health and education cess
    print("Net income after tax = Rs." + str(taxable_income))

# if salary is from Rs.2,50,001 to Rs.5,00,000

elif total_income >= 250001 and total_income <= 500000:
    if age <= 60:  # for age less than or equal to 60 ,Sex may be either M or F
        taxable_income = (total_income - (total_income * .05))  # Deducting 5% of total income
        taxable_income = taxable_income - investment_amount  # Deducting investment amount from remaining
        taxable_income = taxable_income - (taxable_income * .04)  # Deducting 4% of Health and education cess
        print("Net income after  tax  = Rs." + str(taxable_income))
    else:
        if sex.upper() == "F" and age > 60:  # for age greater than to 60 ,Sex must be F
            taxable_income = (total_income - (total_income * .03))  # Deducting 3% of total income
            taxable_income = taxable_income - investment_amount  # Deducting investment amount from remaining
            taxable_income = taxable_income - (taxable_income * .04)  # Deducting 4% of Health and education cess
            print("Net income after  tax  = Rs." + str(taxable_income))

# if salary is from Rs.5,00,001 to Rs.10,00,000
elif total_income >= 500001 and total_income <= 1000000:
    if age <= 60:  # for age less than or equal to 60 ,Sex may be either M or F
        taxable_income = (total_income - (total_income * .2) - 12500)  # Deducting 20% of total income and deducting Rs.12,500
        taxable_income = taxable_income - investment_amount  # Deducting investment amount from remaining
        taxable_income = taxable_income - (taxable_income * .04)  # Deducting 4% of Health and education cess
        print("Net income after tax  = Rs." + str(taxable_income))
    else:
        if sex.upper() == "F" and age > 60:  # for age greater than to 60 ,Sex must be F
            taxable_income = (total_income - (total_income * .2) - 7500)  # Deducting 20% of total income and deducting Rs.7,500
            taxable_income = taxable_income - investment_amount  # Deducting investment amount from remaining
            taxable_income = taxable_income - (taxable_income * .04)  # Deducting 4% of Health and education cess
            print("Net income after tax  = Rs." + str(taxable_income))

# if salary if greater that Rs.1000000
elif total_income > 1000000:
    if age <= 60:  # for age less than or equal to 60 ,Sex may be either M or F
        taxable_income = (total_income - (total_income * .3) - 112500)  # Deducting 30% of total income and deducting Rs.1,12,500
        taxable_income = taxable_income - investment_amount  # Deducting investment amount from remaining
        taxable_income = taxable_income - (taxable_income * .04)  # Deducting 4% of Health and education cess
        print("Net income after  tax  = Rs." + str(taxable_income))
    else:
        if sex.upper() == "F" and age > 60:  # for age greater than to 60 ,Sex must be F
            taxable_income = (total_income - (total_income * .3) - 107500)  # Deducting 30% of total income and deducting Rs.1,07,500
            taxable_income = taxable_income - investment_amount  # Deducting investment amount from remaining
            taxable_income = taxable_income - (taxable_income * .04)  # Deducting 4% of Health and education cess
            print("Net income after tax  = Rs." + str(taxable_income))



