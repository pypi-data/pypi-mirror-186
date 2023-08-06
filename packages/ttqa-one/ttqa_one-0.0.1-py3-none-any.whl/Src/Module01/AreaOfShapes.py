
def Cir (radius):
    #Calculates the area of circle 
    arc = 3.14*radius*radius
    print("Area of Circle is ", arc)


def Rect (length, width):
    #Calculates the area of Rectangle 
    arr = length * width
    print("Area of Rectangle is ", arr)


def Sqr (side):
    #Calculates the area of Square 
    ars = side ** 2
    print("Area of Square is ", ars)

    
def Tri (base, height):
    #Calculates the area of Triangle 
    art = 0.5 * (base * height)
    print("Area of triangle is ", art)

Cir(2)
Rect(25, 20)
Sqr(30)
Tri(30, 30)