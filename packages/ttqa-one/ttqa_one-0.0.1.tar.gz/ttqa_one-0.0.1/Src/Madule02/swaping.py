#This program swaps the 1st and last elements of a list

def Swap(mylist):
    size = len(mylist)
    temp = mylist[0]
    mylist[0] = mylist[size-1]
    mylist[size-1] = temp

    return mylist

lista = [12, 23, 45, 95, 10]
print('Original list: ', lista)
print('List after swaping: ', Swap(lista))