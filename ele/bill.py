# Eb reading

# ct      u                 chr

# House  <500              0.75
#        >=500 and <1000   1.25
#        >=1000            1.75

# Shop   <1000              2.00
#        >=1000 and <2500   3.00
#        >=2500             4.00

# inudstry  <2500               4.00
#           >=2500 and <4000     6.00
#           >=4000               7.50

customer_type = str(input("Enter customer type, Home/Shop/Industry: ")).lower()
unit = float(input('Enter electricity measure: '))

def updaateData(customer_arg, bill_arg, unit_arg):
    customer_text = f'Customer type: {customer_arg}\n'
    bill = f'customer used unit: {unit_arg}, Total bill: {bill_arg}'    
    f = open(f"{customer_arg}.txt", "a")
    f.write(customer_text)
    f.write(bill)
    f.close()
    
    r = open(f"{customer_arg}.txt", "r")
    print(r.read())


if customer_type == 'house':

    if unit < 500:
        bill = 0.75 * unit
    elif unit >= 500 and unit < 1000:
        bill = 1.25 * unit
    elif unit >= 2500:
        bill = 1.7 * unit
    updaateData(customer_type, bill, unit)
elif customer_type == 'shop':
    if unit < 1000:
        bill = 2.00 * unit
    elif  1000 <= unit < 2500:
        bill = 3.00 * unit
    elif unit >= 2500:
        bill = 4.00 * unit
    updaateData(customer_type, bill, unit)
elif customer_type == 'industry':
    if unit < 2500:
        bill = 4.00 * unit
    elif 2500 <= unit < 4000:
        bill = 6.00 * unit
    elif unit >= 4000:
        bill = 7.50 * unit
    updaateData(customer_type, bill, unit)