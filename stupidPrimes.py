from datetime import datetime


# POBRAĆ GÓRNY ZAKRES
# SPRAWDZAĆ KAŻDĄ LICZBĘ PO KOLEI
# DLA KAŻDEJ LICZBY OKREŚLIĆ CZY JEDYNYM DZIELNIKIEM JEST 1 I LICZBA SPRAWDZANA
# WYNIK ZAPISAĆ DO TABLICY ( 0,1)
# SPRAWDZIĆ CZY 1 WYSTĘPUJE 2 RAZY , JEŚLI TAK TO LICZBA PIERWSZA


zakres = int(input('Please input max number : '))
primes = []
primeMatrix=[]

def isPrime(liczba):
    state = 0
    if liczba <2:
        print('NUmber is to low to check for prime, less than 2')
    if liczba >=2:
        x=liczba
        while x>=1:
            if liczba%x==0:
                primeMatrix.append(1)
                
            else:
                primeMatrix.append(0)
            x-=1
        
    if primeMatrix.count(1)==2:
        state = 1
    else:
        state = 0
    primeMatrix.clear()
    return state

start_time = datetime.now()
while zakres>=2:
    if isPrime(zakres) == 1:
        primes.append(zakres)
        

    zakres-=1
end_time = datetime.now()
print(primes)
print('Executed in: {}'.format(end_time-start_time))









