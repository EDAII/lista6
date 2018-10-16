import random

vetor = []
vetortorre=[]
tam = int(input("insira o tamanho do vetor \n"))
vetor = random.sample(range(10000000), tam)
ordenavetor = sorted(vetor)
print(ordenavetor)
n=int(input("alcance da torre\n"))

for i in range(tam): 
   if(i==0): 
       print("precisa de outra torre") 
       vetortorre.append(ordenavetor[i]+n)  
       print(str(vetortorre[i]))
       i2=0       
   if(ordenavetor[i]-vetortorre[i2]>n): 
         vetortorre.append(ordenavetor[i]+n)
         print(str(ordenavetor[i]))          
         i2=i2+1  
x=[]
y=[]
x=ordenavetor
print(vetortorre)
for n2 in vetortorre:
     y.append(n2-n)
     y.append(n2+n)
                                  	        
print(y)
print(x)           
