# 121, 13431, 54345 Are P121alindrome numbers


i = 0
for num in range(100,201):
    
    r = num % 10
    
    i = i + r**3

    num = num // 10  
print(i , end=" ")
    
    
