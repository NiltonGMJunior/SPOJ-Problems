#   Nilton G. M. Junior
#   04/12/2018
#   Sphere Online Judgment
#   PRIME1 - Prime Generator
#   https://www.spoj.com/problems/PRIME1/

# TODO: Sieve is taking too long (Time Limit Exceeded). Needs faster algorithm

def isPrime(n):
    if n == 2 or n == 3: return True
    if n % 2 == 0 or n < 2: return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def main():
    try:
        num_runs = input()
        for i in range(num_runs):
            [start, end] = list(map(int, input().split()))
            for j in range(start, end + 1):
                if isPrime(j):
                    print(j)
            print('')
    except EOFError:
        pass

if __name__ == '__main__':
    main()
