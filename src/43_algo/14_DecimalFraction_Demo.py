from decimal import Decimal

n1 = 1.2
n2 = 1.0

# Must print True, however it shows False due to rounding off error, due to floating point arithmetic
# The errors in Python float operations are inherited from the floating-point hardware
# This is because, most decimal fractions cannot be represented exactly as binary fractions.
# A consequence is floating-point numbers are only approximated by the binary floating-point numbers
# floats are approximated using a binary fraction
print((n2 - n1) == 0.2)

# Solutions 1:
# Round off the results
print("(round(n2) - round(n1)) == round(0.2): {} - {} = {}".format(round(n2),round(n1), round(0.2)))

# Solutions 2:
# Use Decimal datatype to handle precision
# The Decimal has a default precision of 28 places, while the float has 18 places.
# The Decimal type provides several rounding options https://zetcode.com/python/decimal/
print((Decimal('1.2') - Decimal('1.0')) == Decimal('0.2'))

# ******************************************************************************************

# Fractions
from fractions import Fraction
u = Fraction(1) / Fraction(3)
v = u * Fraction(3) # outputs 1

