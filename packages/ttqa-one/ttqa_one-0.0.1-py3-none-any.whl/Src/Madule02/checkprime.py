def checkprime():
    print("Enter a number ")
    try:
        nbr = int(input())
        count = 0
    except:
        print("The number must be of integer type")
    else:
        if(nbr > 1):
            for i in range(1, nbr + 1):
                if(nbr % i == 0):
                    count+=1
            if(count == 2):
                print('Number is prime')
            else:
                print("The number is not prime")

checkprime()
