# for making a and b integer typecasting is required and this could be done in two ways
'''
1_use typecasting in another line as a=int(a)
'''

a=(input('what is your profit'))
b=(input('what was the cost price'))
a=int(a)
b=int(b)
selling_price =(a+b)
print(selling_price)

"""
2_use typecasting in staring while filling data in varible 
like a=(int(input('what is your profit'))) this is the more prefered way 
"""

a=int((input('what is your profit')))
b=int((input('what was the cost price')))
selling_price =(a+b)
print(selling_price)