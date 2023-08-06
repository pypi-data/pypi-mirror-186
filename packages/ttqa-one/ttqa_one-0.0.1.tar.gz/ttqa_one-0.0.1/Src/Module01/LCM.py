#This program calculates the lcm of 2 numbers

def Lcm():
    print('Enter two \'integers\' \n')
    try:
        num1 = int(input("Enter first number\n"))
        num2 = int(input("Enter second number\n"))
    except:
        print("The numbers must be of integer type")
    else:
        maxnbr = max(num1, num2)
        while(True):
            if(maxnbr % num1 == 0 and maxnbr % num2 == 0):
                break
            maxnbr+=1
    print('The lcm of given numbers is', maxnbr)
    
Lcm()