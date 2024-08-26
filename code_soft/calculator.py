a=int(input(("Enter\n 1.Addition\n 2.Subtraction\n 3.Multiplication\n 4.Division\n 5.Remainder ")))
n="yes"
while(n=="yes"):
    v= int(input("enter the first value = "))
    v2= int(input("enter the second value = "))
    if a==1:
        print(f"sum of {v} and {v2} = {v+v2}")
        
    elif a==2:
        print(f"subtraction of {v} and {v2} = {v-v2}")
        
    elif a==3:
        print(f"Multiplication of {v} and {v2} = {v*v2}")
       
    elif a==4:
        print(f"Division of {v} and {v2} = {v/v2}")
        
    elif a==5:
        print(f"Remainder of {v} and {v2} = {v%v2}")
        
    n =input("enter yes to do more calculations = ")
    if n=="yes":
        a=int(input(("Enter\n 1.Addition\n 2.Subtraction\n 3.Multiplication\n 4.Division\n 5.Remainder ")))
    else:
        print("thank you ")


