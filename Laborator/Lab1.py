# #Problema 8
# n = int(input())
# sum = n
# for i in range(1,n):
#     x = int(input())
#     sum=sum^x^i
# print(sum)

# #Problema 9
# n = int(input())
# k = int(input())
# b = int(input())
# print(bin(n))
# mask=1<<(k-1)
# if b == 1:
#     n = n|mask
# else:
#     if n & mask:
#         n = n^mask
#     else:
#         pass
# print(bin(n))

#Problema 10

def afis(ind):
    for i in range(1,n+1):
        if ind&1 :
            print(list[i],end=" ")
        ind=ind>>1
    print()

n = int(input())
list = [0]
for i in range(1,n+1):
    list.append(i)
ind = 0
for i in range(0,2**n):
    afis(ind)
    ind += 1
        