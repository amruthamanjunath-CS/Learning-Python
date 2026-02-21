def is_prime(n):
    if n <= 1:
        return False
    
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    
    return True

left=int(input("Enter the first number:"))
right=int(input("Enter the second number:"))
prime=0

for i in range(left,right+1):
    
    numbers=bin(i)
    count=numbers.count("1")
    
    
    if is_prime(count):
        prime+=1
    
print(prime)    


