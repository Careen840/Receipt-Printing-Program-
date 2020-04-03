# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 01:18:43 2020

@author: Careen Evans
"""


# create a product and price for three items 
p1_name, p1_price = "Apples", 4.50 
p2_name, p2_price ="Toilet Papers",2.99  
p3_name, p3_price = "Mask", 8.99


 # creating a company name and information 
company_name = "Rewe Supermarket" 
company_address = "81768 Lucile Grahn Street 44." 
company_city = "Munchen, Germany"

# display the ending message 
message = "Thanks for choosing Rewe!"

# creating the top border 
print( "*" * 50 )

##displaying company details
print(f"\t\t{company_name.title()}")
print(f"\t\t{company_address}")
print(f"\t\t{company_city}")

## separating between sections
print("-"*50)

 # print out header for section of items 
print("\tProduct Name\tProduct Price")

print(f"\t{p1_name.title()}\t\t${p1_price }") 
print(f"\t{p2_name.title()}\t${p2_price}") 
print(f"\t{ p3_name.title()}\t\t${p3_price }")


# print a line between sections
print('=' * 50)

##print out header for section of total
print("\t\t\tTotal")

# calculate total price and print out 
total_price = p1_price + p2_price + p3_price 
print(f"\t\t\t${total_price}")

# print a line between sections 
print( "=" * 50)

# printing a thank you message
print( f"\n\t{message}\n")


## creating the bottom border
print("*" * 50)
