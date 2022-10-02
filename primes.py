"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):




    list = []
    freq= {}


    num = 2

    if number_of_primes <= 0:
        raise ValueError ("Only use numbers > 0")

    else:

        list.append(2)
        amountOfPrimes = 1
        while amountOfPrimes < number_of_primes:
            num += 1
            prime = True


            for y in range(2,num):
                if (num%y==0):
                    prime = False
            if prime:
                if num in freq:
                    freq[num] +=1
                else:
                    amountOfPrimes += 1
                    list.append(num)
                    freq[num] = 1

    return list
