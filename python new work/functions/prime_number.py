#def is_prime (num) return true if num is prime else return false
def is_prime(num):
    for n in range(2,num+1):
        if num%n==0:
            return False
        else:
            return True
print(is_prime(19)) 