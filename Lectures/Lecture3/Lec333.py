def func(*kids):
    print(kids[0])


x= lambda a,b :a+b
print(x(2,3))



x=33
y=33

print ("x") if x > y else print ("yhhhhhhh") if x == y else print ("y")

[print(i) for i in range(300) if i%2==0]

def func(**kids):
    print(kids["first"])
    print(kids["secound"])
    print(kids["third"])

func(third="wdqd",secound="basjhxbja",first="jqeiocjmqe")

dictio=dict(third="wdqd",secound="basjhxbja",first="jqeiocjmqe") # Pack
func(**dictio) #unpack
