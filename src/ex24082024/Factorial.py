# factorial program, it works with integer numbers

# 5 -> 5*4*3*2*1 = 120

num = int(input("Enter the int number : "))
fact = 1
if num == 0 or num == 1:
    fact = 1
    print(1)
else:
    for i in range(1,num+1,1):
        fact = fact * i
        print(fact)
'''
i = 1
while i<=num:ˍ
    fact=fact*i
    i=i+1
    print(fact)

'''