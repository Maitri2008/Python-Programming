# WAP to input a no. and print it's table

# Taking input for the num
num=int(input("Enter a no. to print it's table: "))

#Using loop to print it's table
for i in range(1,11):
    print(f"{num} x {i} = ",num*i)

"""
----------------------------SAMPLE OUTPUT----------------------------
Enter a no. to print it's table: 4
4 x 1 =  4
4 x 2 =  8
4 x 3 =  12
4 x 4 =  16
4 x 5 =  20
4 x 6 =  24
4 x 7 =  28
4 x 8 =  32
4 x 9 =  36
4 x 10 =  40
----------------------------------------------------------------------
