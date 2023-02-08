# def greet(x="default",y="default"):
#     print("Hello  "+x+"   !   "+y)
    
# greet(y="ggggg",x="dwqdq")

# greet()

##########################################

# def func():
#     aString= "mohamed"
#     aNumber= 25
    
#     return aString ,aNumber

# name,age=func()

# print(name,age)
##########################################
#SWAP 
# def func(x,y):
#     return y,x

# x=int(input("Enter 1 to add item to the list "))
# y=int(input("Enter 1 to add item to the list "))
# print(x,y)
# x,y=func(x,y)
# print(x,y)
    
##########################################


# print("Enter 1 to add item to the DO list ")
# print("Enter 2 to print the DO list ")
# print("Enter 3 to mark item as done ")
# print("Enter 4 to print the done list ")
# print("##########################################")
# Mainlst=[]
# Donelst=[]

# while True:
#     x=int(input("Enter your choise : "))
#     if x==1:
#         y=str(input("type your item : "))
#         Mainlst.append(y)
#     elif x==2:
#         print(Mainlst)
#     elif x==3:
#         z=int(input("type the number of item to be marked : "))
#         Donelst.append(Mainlst[z-1])
#         del Mainlst[z-1]
#     elif x==4:
#         print(Donelst)


##########################################


# import BIT_MATH as bm

# def main():

#     x=bm.SET_BIT(5,1)
#     print(x)
    
# if __name__ == "__main__":
#     main()


    
##########################################
#copying with different adresses
# lst1=list(range(10))

# lst2=lst1
# lst1[0]=50000
# print(lst1,lst2)


# lst2=lst1.copy()
# lst1[0]=3333333
# print(lst1,lst2)

##########################################



lst1=[['aaaa',30],['bbbb',40],['cccc',30]]


for i in lst1:
    name+=i[0]
    degree+=i[1]
    




