
def tobinary(number):
   if number == 0:
       print('0000')
    
   binary=''
   while number>0:
       reminder=number%2
       binary=str(reminder) + binary 
       number//=2
    
   while len(binary) %4 !=0:
       binary='0'+binary  
       
   groubed=" ".join(binary[i:i+4] for i in range(0,len(binary),4))
   
   return groubed

number=int(input("enter number to converted to binary: "))   
print(tobinary(number))    
    