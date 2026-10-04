# WAP to input selling price & cost price of a product. Caculate the profit amount & percentage of profit 
# (Assuming there is Profit)

# Taking input for Cost price and Selling price

sp=int(input("Enter Selling Price: "))
cp=int(input("Enter Cost Price: "))

# Calculating Profit Amount & Profit Percentage 

amnt=sp-cp
prctg=(amnt/cp)*100

# Printing Profit Amount & Profit Percentage

print("Profit Amount:",amnt)
print("Profit Percentage:",prctg)

"""
----------------------SAMPLE OUTPUT-------------------
Enter Selling Price: 1000
Enter Cost Price: 600
Profit Amount: 400
Profit Percentage: 66.66666666666666
------------------------------------------------------
"""
