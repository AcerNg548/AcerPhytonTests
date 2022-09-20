#3x3 matrix calculator

print("This is a 3 by 3 matrix determinant calculator")

print("\n")
print("a	b	c\na1	b1	c1\na2	b2	c2")

a =  int(input("Please enter the value of a: "))
b=  int(input("Please enter the value of b: "))
c =  int(input("Please enter the value of c: "))
a1 =  int(input("Please enter the value of a1: "))
b1 =  int(input("Please enter the value of b1: "))
c1 =  int(input("Please enter the value of c1: "))
a2 =  int(input("Please enter the value of a2: "))
b2 =  int(input("Please enter the value of b2: "))
c2 =  int(input("Please enter the value of c2: "))

print("\n")


#demand
d = (a * b1 * c2)
d1 = (b * c1 * a2)
d2 = (a1 * b2 * c)

#supply
s = (a2 * b1 * c)
s1 = (a1 * b *c2)
s2 = (b2 * c1 * a)

det = ((d + d1 + d2) - (s + s1 + s2))

print("\n")
print("Dear User your determinant to your 3x3 matrix is :", det)
print("\n")
print(":) code written by AcerNg548\n\nCourtsey to Mr. Biola Olabode")