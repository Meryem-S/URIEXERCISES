a,b,c=input("Enter A,B and C space-separated\n").split()
a,b,c=float(a),float(b),float(c)
pi=3.14159
triangle=a*c/2
circle=pi*c**2
trapezoid=0.5*(a+b)*c
square=b**2
rectangle=a*b
print("TRIANGLE: {:.3f}".format(triangle),"CIRCLE: {:.3f}".format(circle),"TRAPEZOID: {:.3f}".format(trapezoid),"SQUARE: {:.3f}".format(square),"RECTANGLE: {:.3f}".format(rectangle),sep="\n")