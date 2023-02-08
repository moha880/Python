def SET_BIT(VAR,BIT):
    VAR=int(VAR)
    BIT=int(BIT)
    result=VAR|(1<<BIT)
    return result
    
    
def CLR_BIT(VAR,BIT):
    VAR=int(VAR)
    BIT=int(BIT)
    result=VAR & (~(1<<BIT))
    return result

    
    
def TOG_BIT(VAR,BIT):
    VAR=int(VAR)
    BIT=int(BIT)
    result=VAR^(1<<BIT)
    return result

    
def GET_BIT(VAR,BIT):
    VAR=int(VAR)
    BIT=int(BIT)
    result=(VAR >> BIT) & 1
    return result

 
 
if __name__ == "__main__":
    x=10
    x=SET_BIT(x,2)
    print(x)
    