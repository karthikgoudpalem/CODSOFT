def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div (a,b):
    if b != 0 :
        return a/b
    else:
        return "can't divide by 0"

print("select the option:")
print("1.add")
print("2.sub")
print("3.mul")  
print("4.div")

select= input("select(1/2/3/4):")
value1= float(input("enter first value: "))
value2= float(input("enter second value: "))



if select=="1":
    print(value1,"+",value2,"=", add(value1,value2))
elif select=="2":
    print(value1,"-",value2,"=", sub(value1,value2))
elif select=="3":
    print(value1,"*",value2,"=", mul(value1,value2)) 
elif select=="4":
    print(value1,"/",value2,"=", div(value1,value2)) 
else:
    print("select a valid number")          

