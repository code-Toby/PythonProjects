import random

f = open("key.txt",'w')







MainInt = 0


def Main_menu():
   if MainInt == 0:
        print("""



        --------------------
        S&box KeyGen
        1. Generate key
        2. exit
        --------------------




        """)
   if MainInt == 1:
        print("""



        --------------------
        S&box KeyGen
        1. Generate key
        2. save-code
        3. exit
        --------------------




        """)

while True:
    Main_menu()
    reply = int(input())
    
    Int1 = random.randint(1000,9999)
    Int2 = random.randint(1000,9999) 
    Int3 = random.randint(1000,9999) 

    Code1 = str(Int1)
    Code2 = str(Int2)
    Code3 = str(Int2)

    



    if reply == 1:
     lastCode = "Code: "+Code1+"-"+Code2+"-"+Code3
     print("----------------")   
     print(lastCode)
     print("----------------")
     MainInt = 1
    elif reply == 2:
        if MainInt == 0:
            exit()
            
        if MainInt == 1:
            print("Saved-Code: "+lastCode)
            f.write("Code: "+lastCode)
    elif reply == 3:
        if MainInt == 1:
           exit()
           
        
