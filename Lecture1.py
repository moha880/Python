# # print('gg')
# # print("i said:'gg'")

# # x=str(input('please enter value: '))
# # print(x)
# # print(type(x))
# print('gg')

# #type()

# age=int(input('enter age : '))
# print(f'you are {age} years old')


# list=['ahmed','waleed','said']
# passwords=[1111,2222,3333]
# name=input('please enter name :')
# if(name in list):
#     password=int(input('please enter password:'))
#     if(password == passwords[list.index(name)]):
#         print(f'welcome {name}')
#     else:
#         print('wrong password')
# else:
#     print('invalid username')
    
name=input('please enter name :')
name2=''
name3=''
for i in range(len(name)):
    print(name[i]) 
    name2=name[i]+name2
    name3+=name[len(name)-i-1]
    
print(name2) 
print(name3) 

    