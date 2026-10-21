"""
check if zero, even, odd

"""
    
from os import system
def main()->None:
	system("cls")
    
    try:
        a:int=int(input("Enter a value: "))
        if a==0:
            print("Zero")
        elif (a%2)==0:
            print("Even")
        else: 
            print("Odd")       
    except Exception as e:
        print("Invalid")
        
if __name__=="__main__": 
    main()