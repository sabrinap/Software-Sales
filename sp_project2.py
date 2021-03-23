# ==============================================================================
# PROGRAM Software Sales
# PROJECT NUMBER: 2 
# DUE DATE: Tuesday 9/24/2019
# PLATFORM: Windows OS / Python 3
# 
# SUMMARY
#
# Write a program that asks the user to enter the number of units sold
# (as a whole number) and calculates the total cost of the purchase.
# Output the cost per unit after the discount is calculated, as well as
# the total price of the whole sale.
#
# OUTPUT
#
# The program prints an output title, echoprints the user's input in
# a readable fashion, and then prints out the calculated results.
#
# ASSUMPTIONS
#
# We assume that input data is valid and correctly entered by the user.
# The program is guaranteed to warn user from invalid data entered and
# end program.
# ==============================================================================

# named constants
RETAIL_PRICE = 99 # Original cost of unit
DISCOUNT_1 = 0.20 # 20% off applied to original cost of unit 
DISCOUNT_2 = 0.30 # 30% off applied to original cost of unit
DISCOUNT_3 = 0.40 # 40% off applied to original cost of unit
DISCOUNT_4 = 0.50 # 50% off applied to original cost of unit

# print introductory program output heading
print ('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
print ('Welcome to the Software Sales Calculator')
print ('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n')

print ('Retail Price $99')
print ('Buy 10 to 19 units and you get 20% off')
print ('Buy 20 to 49 units and you get 30% off')
print ('Buy 50 to 99 units and you get 40% off')
print ('Buy 100 or more units and you get 50% off')

print ('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n')

# read the amount of units sold from user
unitsSold = int(input('How many units were sold? '))

if unitsSold >= 100:
        #discount calculations for 50%
        discount = DISCOUNT_4 * RETAIL_PRICE
        discountTotal = RETAIL_PRICE - discount
        print ('With the discount your effective cost per unit is $%.2f' % discountTotal)
        #grandtotal calculation
        grandTotal = unitsSold * discountTotal
        print ('The total cost of the purchase is $%.2f\n' % grandTotal)
        # print closing message
        print ('Execution Terminated Normally.')
       
elif unitsSold >= 50:
        #discount calculations for 40%
        discount = DISCOUNT_3 * RETAIL_PRICE
        discountTotal = RETAIL_PRICE - discount
        print ('With the discount your effective cost per unit is $%.2f' % discountTotal)
        #grandtotal calculation
        grandTotal = unitsSold * discountTotal
        print ('The total cost of the purchase is $%.2f\n' % grandTotal)
        # print closing message
        print ('Execution Terminated Normally.')
       
elif unitsSold >= 20:
        #discount calculations for 30%
        discount = DISCOUNT_2 * RETAIL_PRICE
        discountTotal = RETAIL_PRICE - discount
        print ('With the discount your effective cost per unit is $%.2f' % discountTotal)
        #grandtotal calculation
        grandTotal = unitsSold * discountTotal
        print ('The total cost of the purchase is $%.2f\n' % grandTotal)
        # print closing message
        print ('Execution Terminated Normally.')

elif unitsSold >= 10:
        #discount calculations for 20%
        discount = DISCOUNT_1 * RETAIL_PRICE
        discountTotal = RETAIL_PRICE - discount
        print ('With the discount your effective cost per unit is $%.2f' % discountTotal)
        #grandtotal calculation
        grandTotal = unitsSold * discountTotal
        print ('The total cost of the purchase is $%.2f\n' % grandTotal)
        # print closing message
        print ('Execution Terminated Normally.')

elif unitsSold >= 1:
        #grandtotal calculation
        grandTotal = unitsSold * RETAIL_PRICE
        print ('No discount was added. Your effective cost per unit is $%.2f' % RETAIL_PRICE)
        print ('The total cost of the purchase is $%.2f\n' % grandTotal)
        # print closing message
        print ('Execution Terminated Normally.')

else:
    print ('Units sold must be greater than zero. Ending program run\n')
    # print closing message
    print ('Execution Terminated Normally.')
    
# ==============================================================================
#                              END OF PROGRAM
# ==============================================================================

