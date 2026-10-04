# WAP to input selling price & cost price of an item and tell if there is PROFIT, LOSS
# or NO PROFIT & NO LOSS

# Taking input for the Selling Price and Cost Price

cp=int(input("Enter Cost Price: "))
sp=int(input("Enter Selling Price: "))

# Checking whether item is sold at PROFIT, LOSS or NO PROFIT & NO LOSS

if(sp>cp):
    print("Item sold at a PROFIT of ",sp-cp)
elif(sp<cp):
    print("Item sold at a LOSS of ",cp-sp)
else:
    print("Item sold at NO PROFIT & NO LOSS")

"""
-----------------------SAMPLE OUTPUT-----------------------
Enter Cost Price: 2500
Enter Selling Price: 8000
Item sold at a PROFIT of  5500
-----------------------------------------------------------
"""
