isbn = input()
isbn = [x for x in isbn if '0'<=x<='9']
sum = sum([(11-(i+1))*int(x) for i,x in enumerate(isbn)])
p=0
while (sum+p)%11!=0:
    p+=1
print(p)