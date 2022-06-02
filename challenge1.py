def productChecker (numList):
    x = 1
    for num in numList:
        x = x * num
    return x
    
def findPrimeList(num):
    primeList=[2]
    x = 3
    y = 0

    while len(primeList) < num:
        for prime in primeList:
            y = x % prime
            if y == 0:
                x+=1
                break
            if (y != 0) and (prime == primeList[-1]):
                primeList.append(x)
                x += 1
                break
    return primeList
            
def get_prime_factors(num):
    x = num
    prime_factors = []
    prime_numbers = findPrimeList(10)
    while productChecker(prime_factors) != num:
        for prime_number in prime_numbers:
            if (x % prime_number ==0):
                prime_factors.append(prime_number)
                x = x / prime_number
                break
    print(prime_factors)
        
get_prime_factors(98)