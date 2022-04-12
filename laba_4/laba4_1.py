n=int(input ('Введите количество элементов последовательности: '))
x=1 
s=0 
print(x)
for i in range(n):
    print("x=",x, '   Сумма ряда s=',s)
    s+=x 
    x/=-2
   
