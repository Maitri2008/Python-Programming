# WAP to calculate electricity based on the units consumed

""" GIVEN: 0-200 units Rs.0 per unit
           201-400 units Rs.4 per unit
           401-600 units Rs.6 per unit
           601-800 units Rs.8 per unit
           units>=800 Rs.10 per unit """
# Taking input for the units

units=eval(input("Enter no. of units: "))

# Calculating the bill based on the units

bill=0

if(units<=400):
    bill=(200*0)+((units-200)*4)
elif(units<=600):
    bill=(200*0)+(200*4)+((units-400)*6)
elif(units<=800):
    bill=(200*0)+(200*4)+(200*6)+((units-600)*8)
else:
    bill=(200*0)+(200*4)+(200*6)+(200*8)+((units-800)*10)

# Printing the Bill based on Units

print("Units Consumed:",units)
print("Bill Calculated:",bill)

"""
-------------------SAMPLE OUTPUT-------------------
Enter no. of units: 542
Units Consumed: 542
Bill Calculated: 1652
---------------------------------------------------
"""
